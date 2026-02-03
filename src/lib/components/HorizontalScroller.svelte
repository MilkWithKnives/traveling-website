<script lang="ts">
  import { onMount, onDestroy, setContext } from 'svelte';
  import { activeIndex, scrollerHandle } from '$lib/stores/scroller.js';

  let rail: HTMLDivElement | null = null;
  const prefersReduced =
    typeof window !== 'undefined' && window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  const scrollToIndex = (i: number, behavior: ScrollBehavior = prefersReduced ? 'auto' : 'smooth') => {
    if (!rail) return;
    const width = rail.clientWidth;
    rail.scrollTo({ left: i * width, behavior });
  };

  scrollerHandle.set({ scrollToIndex });
  setContext('scroller-handle', { scrollToIndex });

  const isVertScrollable = (el: EventTarget | null, dy: number) => {
    let node = el as HTMLElement | null;
    while (node && node !== rail) {
      const canScroll = node.scrollHeight > node.clientHeight;
      if (canScroll) {
        if (dy < 0 && node.scrollTop > 0) return true;
        if (dy > 0 && node.scrollTop + node.clientHeight < node.scrollHeight) return true;
      }
      node = node.parentElement;
    }
    return false;
  };

  const wheelHandler = (e: WheelEvent) => {
    if (!rail) return;
    if (isVertScrollable(e.target, e.deltaY)) return;
    e.preventDefault();
    rail.scrollLeft += e.deltaY;
  };

  const keyHandler = (e: KeyboardEvent) => {
    if (!rail) return;
    const width = rail.clientWidth;
    let delta = 0;
    if (e.key === 'ArrowRight' || e.key === 'PageDown') delta = width;
    if (e.key === 'ArrowLeft' || e.key === 'PageUp') delta = -width;
    if (e.key === 'Home') rail.scrollTo({ left: 0, behavior: prefersReduced ? 'auto' : 'smooth' });
    if (e.key === 'End') rail.scrollTo({ left: rail.scrollWidth, behavior: prefersReduced ? 'auto' : 'smooth' });
    if (delta !== 0) {
      e.preventDefault();
      rail.scrollBy({ left: delta, behavior: prefersReduced ? 'auto' : 'smooth' });
    }
  };

  let observer: IntersectionObserver | null = null;

  onMount(() => {
    if (!rail) return;
    rail.addEventListener('wheel', wheelHandler, { passive: false });
    window.addEventListener('keydown', keyHandler);

    observer = new IntersectionObserver(
      (entries) => {
        const visible = entries
          .filter((e) => e.isIntersecting)
          .sort((a, b) => b.intersectionRatio - a.intersectionRatio);
        if (visible[0]) {
          const idx = Number((visible[0].target as HTMLElement).dataset.index ?? '0');
          activeIndex.set(idx);
        }
      },
      { root: rail, threshold: [0.5] }
    );

    Array.from(rail.children).forEach((child, i) => {
      (child as HTMLElement).dataset.index = String(i);
      observer?.observe(child);
    });

    return () => {
      rail?.removeEventListener('wheel', wheelHandler);
      window.removeEventListener('keydown', keyHandler);
      observer?.disconnect();
    };
  });

  onDestroy(() => {
    scrollerHandle.set(null);
  });
</script>

<div
  bind:this={rail}
  class="rail hide-scrollbar"
  style="scroll-behavior: {prefersReduced ? 'auto' : 'smooth'}"
>
  <slot />
</div>

<style>
  .rail {
    display: flex;
    flex-direction: row;
    flex-wrap: nowrap;
    height: 100%;
    width: 100vw;
    overflow-x: auto;
    overflow-y: hidden;
    scroll-snap-type: x mandatory;
    scroll-behavior: smooth;
    -webkit-overflow-scrolling: touch;
  }

  :global(.h-section) {
    flex: 0 0 100vw;
    width: 100vw;
    height: 100vh;
    scroll-snap-align: start;
    scroll-snap-stop: always;
    flex-shrink: 0;
    position: relative;
    padding-top: var(--nav-h);
    box-sizing: border-box;
  }
</style>

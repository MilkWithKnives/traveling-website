<script lang="ts">
  import type { Snippet } from 'svelte';
  import { onMount, onDestroy, setContext } from 'svelte';
  import { activeIndex, scrollerHandle } from '$lib/stores/scroller.js';

  let { children }: { children?: Snippet } = $props();
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

  let wheelAccumulator = 0;
  let wheelResetTimer: ReturnType<typeof setTimeout> | null = null;
  let pendingStep: -1 | 0 | 1 = 0;
  let isSectionAnimating = false;
  let lastWheelAt = 0;

  const getRailWidth = () => rail?.clientWidth ?? 0;
  const getMaxScrollLeft = () => {
    if (!rail) return 0;
    return Math.max(0, rail.scrollWidth - rail.clientWidth);
  };

  const clampIndex = (index: number) => {
    const width = getRailWidth();
    if (!width) return 0;
    const maxIndex = Math.round(getMaxScrollLeft() / width);
    return Math.min(Math.max(0, index), maxIndex);
  };

  const normalizeAxisDelta = (delta: number, deltaMode: number) => {
    // deltaMode: 0=pixel, 1=line, 2=page
    if (deltaMode === 1) return delta * 16;
    if (deltaMode === 2) return delta * (getRailWidth() || window.innerWidth);
    return delta;
  };

  const clearWheelResetTimer = () => {
    if (!wheelResetTimer) return;
    clearTimeout(wheelResetTimer);
    wheelResetTimer = null;
  };

  const waitForSectionSettle = (targetIndex: number) => {
    if (!rail) return;
    const targetLeft = targetIndex * getRailWidth();
    const startedAt = performance.now();
    const timeoutMs = prefersReduced ? 140 : 750;
    const tolerance = 1.5;
    let settledFrames = 0;

    const tick = () => {
      if (!rail) {
        isSectionAnimating = false;
        return;
      }

      const diff = Math.abs(rail.scrollLeft - targetLeft);
      if (diff <= tolerance) {
        settledFrames += 1;
      } else {
        settledFrames = 0;
      }

      const elapsed = performance.now() - startedAt;
      if (settledFrames >= 2 || elapsed >= timeoutMs) {
        isSectionAnimating = false;
        const idleFor = performance.now() - lastWheelAt;
        if (pendingStep !== 0 && idleFor < 140) {
          const step = pendingStep;
          pendingStep = 0;
          applyStep(step);
          return;
        }
        pendingStep = 0;
        return;
      }

      requestAnimationFrame(tick);
    };

    requestAnimationFrame(tick);
  };

  const applyStep = (step: -1 | 1) => {
    if (!rail || isSectionAnimating) return;
    const width = getRailWidth();
    if (!width) return;

    const currentIndex = clampIndex(Math.round(rail.scrollLeft / width));
    const targetIndex = clampIndex(currentIndex + step);
    if (targetIndex === currentIndex) {
      return;
    }

    isSectionAnimating = true;
    scrollToIndex(targetIndex);
    waitForSectionSettle(targetIndex);
  };

  const wheelHandler = (e: WheelEvent) => {
    if (!rail) return;
    lastWheelAt = performance.now();

    // Direction contract:
    // down (+deltaY) and right (+deltaX) => forward
    // up (-deltaY) and left (-deltaX) => backward
    const directionalDelta =
      normalizeAxisDelta(e.deltaX, e.deltaMode) + normalizeAxisDelta(e.deltaY, e.deltaMode);

    if (!Number.isFinite(directionalDelta) || directionalDelta === 0) return;
    e.preventDefault();

    if (wheelAccumulator !== 0 && Math.sign(wheelAccumulator) !== Math.sign(directionalDelta)) {
      wheelAccumulator = directionalDelta;
    } else {
      wheelAccumulator += directionalDelta;
    }

    clearWheelResetTimer();
    wheelResetTimer = setTimeout(() => {
      wheelAccumulator = 0;
      pendingStep = 0;
    }, 120);

    const threshold = 140;
    const steps = Math.trunc(wheelAccumulator / threshold);
    if (steps === 0) return;

    const clampedSteps = Math.max(-2, Math.min(2, steps));
    const step: -1 | 1 = clampedSteps > 0 ? 1 : -1;
    wheelAccumulator -= step * threshold;

    if (isSectionAnimating) {
      pendingStep = step;
      return;
    }

    applyStep(step);
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
      clearWheelResetTimer();
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
  {@render children?.()}
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
    touch-action: pan-x;
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

<script lang="ts">
  import HorizontalScroller from '$lib/components/HorizontalScroller.svelte';
  import { scrollerHandle } from '$lib/stores/scroller.js';
  import { get } from 'svelte/store';

  const navLinks = [
    { label: 'Work', id: 'work' },
    { label: 'Journal', id: 'journal' },
    { label: 'Services', id: 'services' },
    { label: 'Schedule', id: 'schedule' },
    { label: 'About', id: 'about' },
    { label: 'Contact', id: 'contact' },
    { label: 'Testimonials', id: 'testimonials' }
  ];

  const cards = {
    redwood: { title: 'Redwood Mist', meta: 'Redwood NP · CA', gradient: 'var(--blue-a), var(--blue-b)' },
    marfa: { title: 'Marfa Dustlight', meta: 'Marfa · TX', gradient: 'var(--orange-a), var(--orange-b)' }
  };

  const testimonials = [
    {
      quote: 'He plans like a producer and shoots like a poet. Our brand launch felt cinematic yet honest.',
      author: 'Camila Duarte',
      role: 'CMO, Azulejo Hotels'
    },
    {
      quote: 'We hiked in the dark to catch first light. The images feel like the trip—windy, real, unforgettable.',
      author: 'Ethan & Mara',
      role: 'Adventure elopement, Faroe Islands'
    },
    {
      quote:
        'Champion, a traveling photographer writing visual essays from the American road under Full Scope Media. Planning like a producer, shooting like a storyteller.',
      author: 'Ryan Champion',
      role: 'Full Scope Media LLC'
    }
  ];

  const scrollToId = (id: string) => {
    const handle = get(scrollerHandle);
    if (!handle || !('scrollToIndex' in handle)) return;
    const el = document.getElementById(id);
    if (!el) return;
    const idx = Number(el.dataset.index ?? 0);
    handle.scrollToIndex(idx);
  };
</script>

<svelte:head>
  <title>Full Scope Media | Horizontal</title>
</svelte:head>

<nav class="top-nav">
  <div class="nav-pill">FULL SCOPE MEDIA</div>
  <div class="nav-links">
    {#each navLinks as link}
      <button class="nav-link" on:click={() => scrollToId(link.id)}>{link.label}</button>
    {/each}
  </div>
  <div class="nav-actions">
    <div class="mini-pill">☼</div>
    <button class="btn primary" on:click={() => scrollToId('contact')}>Book</button>
  </div>
</nav>

<HorizontalScroller>
  <!-- HERO -->
  <section class="h-section hero-section" id="hero">
    <div class="section-frame">
      <div class="hero-grid">
        <div class="hero-col hero-copy">
          <p class="eyebrow">RYAN CHAMPION · FULL SCOPE MEDIA LLC · ROAD DESK USA</p>
          <h1>Editorial stories from the American road—passport ready.</h1>
          <p class="lede">
            Documentary-first imagery with cinematic framing for couples, brands, and publications. Currently traveling
            the United States, booking international work with notice.
          </p>
          <div class="hero-actions">
            <button class="btn primary" on:click={() => scrollToId('work')}>See work</button>
            <button class="btn ghost" on:click={() => scrollToId('journal')}>Read the journal</button>
          </div>
          <p class="meta-line">Now: Southwest (Jan–Mar 2026) · Next: PNW, NYC · International on request</p>
        </div>

        <div class="hero-col cards-stack">
          <div class="card tall blue">
            <div class="card-title">{cards.redwood.title}</div>
            <div class="card-meta">{cards.redwood.meta}</div>
            <div class="pill-tag">Redwood National Park, CA · 2025</div>
          </div>
          <div class="card wide orange">
            <div class="card-title">{cards.marfa.title}</div>
            <div class="card-meta">{cards.marfa.meta}</div>
          </div>
        </div>

        <div class="hero-col selected">
          <p class="eyebrow">Selected work</p>
          <h2>Travel chapters</h2>
          <p class="hint">Curated galleries from recent journeys.</p>
          <div class="selected-grid">
            <div class="card tall blue">
              <div class="card-title">{cards.redwood.title}</div>
              <div class="card-meta">{cards.redwood.meta}</div>
            </div>
            <div class="card tall orange">
              <div class="card-title">{cards.marfa.title}</div>
              <div class="card-meta">{cards.marfa.meta}</div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- WORK -->
  <section class="h-section section" id="work">
    <div class="section-frame">
      <div class="section-inner">
        <p class="eyebrow">Work</p>
        <h2>Gallery placeholder</h2>
        <p class="hint">Add your grid here.</p>
      </div>
    </div>
  </section>

  <section class="h-section section" id="journal">
    <div class="section-frame">
      <div class="section-inner">
        <p class="eyebrow">Journal</p>
        <h2>Stories from the road</h2>
      </div>
    </div>
  </section>

  <section class="h-section section" id="services">
    <div class="section-frame">
      <div class="section-inner">
        <p class="eyebrow">Services</p>
        <h2>Offerings</h2>
      </div>
    </div>
  </section>

  <section class="h-section section" id="schedule">
    <div class="section-frame">
      <div class="section-inner">
        <p class="eyebrow">Schedule</p>
        <h2>Travel calendar</h2>
      </div>
    </div>
  </section>

  <!-- Testimonials rail -->
  <section class="h-section section testimonials" id="testimonials">
    <div class="section-frame">
      <div class="section-inner">
        <p class="eyebrow">Kind words</p>
        <h2>Trusted by couples & brands</h2>
      </div>
      <div class="scroll-container">
        <div class="testimonials-track hide-scrollbar">
          {#each testimonials as t}
            <div class="testimonial-card">
              <blockquote class="quote">“{t.quote}”</blockquote>
              <div class="author-info">
                <p class="author-name">{t.author}</p>
                <p class="author-role">{t.role}</p>
              </div>
            </div>
          {/each}
        </div>
      </div>
    </div>
  </section>

  <section class="h-section section" id="about">
    <div class="section-frame">
      <div class="section-inner">
        <p class="eyebrow">About</p>
        <h2>Ryan Champion</h2>
      </div>
    </div>
  </section>

  <section class="h-section section" id="contact">
    <div class="section-frame">
      <div class="section-inner">
        <p class="eyebrow">Contact</p>
        <h2>Book a shoot</h2>
      </div>
    </div>
  </section>
</HorizontalScroller>

<style>
  .top-nav {
    position: fixed;
    top: 12px;
    left: 16px;
    right: 16px;
    height: var(--nav-h);
    z-index: 10;
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 12px;
    padding: 12px 16px;
    background: rgba(255, 255, 255, 0.92);
    border: 1px solid var(--border);
    border-radius: 18px;
    backdrop-filter: blur(10px);
  }

  .nav-pill {
    padding: 10px 14px;
    border-radius: 999px;
    border: 1px solid var(--border);
    font-weight: 700;
    letter-spacing: 0.08em;
  }

  .nav-links {
    display: flex;
    gap: 12px;
    flex: 1;
    justify-content: center;
    flex-wrap: wrap;
  }

  .nav-link {
    background: transparent;
    border: none;
    padding: 6px 8px;
    color: var(--muted);
    cursor: pointer;
  }

  .nav-actions {
    display: flex;
    align-items: center;
    gap: 10px;
  }

  .mini-pill {
    width: 36px;
    height: 24px;
    border-radius: 999px;
    background: var(--pill);
    display: grid;
    place-items: center;
    font-size: 14px;
  }

  .btn {
    display: inline-flex;
    align-items: center;
    justify-content: center;
    gap: 6px;
    padding: 12px 16px;
    border-radius: 999px;
    font-weight: 600;
    border: 1px solid var(--border);
    cursor: pointer;
    transition: transform 160ms ease, box-shadow 160ms ease, background 160ms ease;
  }

  .btn.primary {
    background: linear-gradient(120deg, #9bffd5, #4ac4ff);
    color: #0c111a;
    border: none;
    box-shadow: 0 10px 30px rgba(74, 196, 255, 0.3);
  }

  .btn.ghost {
    background: var(--pill);
    color: var(--text);
  }

  .h-section {
    padding: calc(var(--nav-h) + 12px) 24px 24px;
  }

  .section-frame {
    position: sticky;
    top: var(--nav-h);
    height: calc(100vh - var(--nav-h));
    display: flex;
    flex-direction: column;
    gap: 16px;
    overflow-y: auto;
    overflow-x: hidden;
  }

  .hero-grid {
    flex: 1;
    display: grid;
    grid-template-columns: minmax(280px, 1fr) minmax(280px, 1fr) minmax(280px, 1fr);
    gap: 28px;
    align-items: start;
    min-height: 0;
  }

  .hero-col {
    min-width: 0;
  }

  .hero-copy h1 {
    margin: 10px 0 16px;
    font-size: clamp(32px, 4vw, 56px);
    line-height: 1.05;
  }

  .lede {
    color: var(--muted);
    max-width: 520px;
  }

  .hero-actions {
    display: flex;
    gap: 12px;
    margin: 16px 0;
  }

  .meta-line {
    color: var(--muted);
    font-size: 14px;
  }

  .cards-stack {
    display: grid;
    grid-template-rows: 1fr 1.1fr;
    gap: 18px;
  }

  .card {
    border-radius: 22px;
    padding: 18px;
    color: #fff;
    box-shadow: var(--shadow);
    position: relative;
    min-height: 180px;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    overflow: hidden;
  }

  .card.tall {
    min-height: 320px;
  }

  .card.wide {
    min-height: 260px;
  }

  .card.blue {
    background: linear-gradient(160deg, var(--blue-a), var(--blue-b));
  }

  .card.orange {
    background: linear-gradient(160deg, var(--orange-a), var(--orange-b));
  }

  .card-title {
    font-weight: 700;
    font-size: 20px;
  }

  .card-meta {
    font-size: 14px;
    opacity: 0.9;
  }

  .pill-tag {
    align-self: flex-start;
    margin-top: 10px;
    padding: 8px 12px;
    background: rgba(255, 255, 255, 0.18);
    border-radius: 999px;
    font-size: 12px;
  }

  .selected {
    display: grid;
    gap: 14px;
    align-content: start;
  }

  .selected-grid {
    display: grid;
    grid-template-columns: repeat(2, minmax(140px, 1fr));
    gap: 14px;
  }

  .eyebrow {
    font-size: 13px;
    letter-spacing: 0.14em;
    text-transform: uppercase;
    color: var(--muted);
  }

  .hint {
    color: var(--muted);
  }

  .section {
    display: flex;
    flex-direction: column;
    gap: 16px;
  }

  .section-inner {
    max-width: 720px;
  }

  /* Testimonials rail */
  .testimonials {
    background: #0a0a0a;
    color: #fff;
  }

  .testimonials .section-inner .eyebrow {
    color: #888;
  }

  .scroll-container {
    overflow: hidden;
    margin: 0 -24px;
  }

  .testimonials-track {
    display: flex;
    gap: 24px;
    padding: 0 24px 20px;
    overflow-x: auto;
    scroll-behavior: smooth;
    -webkit-overflow-scrolling: touch;
    align-items: flex-start;
  }

  .testimonial-card {
    flex: 0 0 400px;
    min-width: 400px;
    background: rgba(255, 255, 255, 0.03);
    border: 1px solid rgba(255, 255, 255, 0.08);
    border-radius: 12px;
    padding: 32px;
    display: flex;
    flex-direction: column;
    gap: 24px;
    transition: all 0.3s ease;
    height: fit-content;
  }

  .testimonial-card:hover {
    background: rgba(255, 255, 255, 0.05);
    border-color: rgba(255, 255, 255, 0.15);
    transform: translateY(-4px);
  }

  .quote {
    font-size: 16px;
    line-height: 1.6;
    color: #e0e0e0;
    font-weight: 300;
    margin: 0;
  }

  .author-info {
    margin-top: auto;
    padding-top: 8px;
    border-top: 1px solid rgba(255, 255, 255, 0.08);
  }

  .author-name {
    font-size: 14px;
    font-weight: 600;
    color: #fff;
    margin-bottom: 4px;
  }

  .author-role {
    font-size: 13px;
    color: #888;
    font-weight: 400;
  }

  @media (max-width: 900px) {
    .hero-grid {
      grid-template-columns: 1fr;
    }
    .cards-stack {
      grid-template-rows: repeat(2, auto);
    }
    .selected-grid {
      grid-template-columns: repeat(auto-fit, minmax(140px, 1fr));
    }
    .testimonial-card {
      flex: 0 0 320px;
      min-width: 320px;
      padding: 24px;
    }
    .scroll-container {
      margin: 0 -16px;
    }
    .testimonials-track {
      padding: 0 16px 20px;
      gap: 16px;
    }
  }
</style>

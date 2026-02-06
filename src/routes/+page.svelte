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
    {#each navLinks as link (link.id)}
      <button class="nav-link" onclick={() => scrollToId(link.id)}>{link.label}</button>
    {/each}
  </div>
  <div class="nav-actions">
    <div class="mini-pill">☼</div>
    <button class="btn primary" onclick={() => scrollToId('contact')}>Book</button>
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
            <button class="btn primary" onclick={() => scrollToId('work')}>See work</button>
            <button class="btn ghost" onclick={() => scrollToId('journal')}>Read the journal</button>
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
          {#each testimonials as t (`${t.author}-${t.role}`)}
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

  <section class="h-section section about-section" id="about">
    <div class="section-frame about-frame">
      <div class="section-inner about-intro">
        <p class="eyebrow">About</p>
        <h2>Ryan Champion</h2>
        <p class="hint">
          I am currently driving a mobile studio across the U.S., producing documentary travel essays and booking
          brand campaigns between road stops.
        </p>
      </div>

      <div class="about-card-wrap">
        <article class="about-me-card">
          <div class="about-me-background"></div>

          <div class="about-me-logo-wrap" aria-hidden="true">
            <img class="about-me-logo" src="/logo.svg" alt="" loading="lazy" />
          </div>

          <div class="about-me-photo-wrap">
            <img
              class="about-me-photo"
              src="/photos/About%20me/about-photo.png"
              alt="Portrait of Ryan Champion"
              loading="lazy"
            />
          </div>

          <div class="about-me-copy">
            <p class="about-me-label">Right now</p>
            <p class="about-me-snippet">
              Building visual essays from the American road while planning international chapters with Full Scope
              Media.
            </p>
          </div>

          <a class="about-me-box about-me-box1" href="https://instagram.com/" aria-label="Instagram link placeholder">
            <span class="about-me-icon">
              <svg viewBox="0 0 30 30" xmlns="http://www.w3.org/2000/svg" class="about-me-svg">
                <path
                  d="M 9.9980469 3 C 6.1390469 3 3 6.1419531 3 10.001953 L 3 20.001953 C 3 23.860953 6.1419531 27 10.001953 27 L 20.001953 27 C 23.860953 27 27 23.858047 27 19.998047 L 27 9.9980469 C 27 6.1390469 23.858047 3 19.998047 3 L 9.9980469 3 z M 22 7 C 22.552 7 23 7.448 23 8 C 23 8.552 22.552 9 22 9 C 21.448 9 21 8.552 21 8 C 21 7.448 21.448 7 22 7 z M 15 9 C 18.309 9 21 11.691 21 15 C 21 18.309 18.309 21 15 21 C 11.691 21 9 18.309 9 15 C 9 11.691 11.691 9 15 9 z M 15 11 A 4 4 0 0 0 11 15 A 4 4 0 0 0 15 19 A 4 4 0 0 0 19 15 A 4 4 0 0 0 15 11 z"
                ></path>
              </svg>
            </span>
          </a>

          <a class="about-me-box about-me-box2" href="https://x.com/" aria-label="X link placeholder">
            <span class="about-me-icon">
              <svg viewBox="0 0 512 512" xmlns="http://www.w3.org/2000/svg" class="about-me-svg">
                <path
                  d="M459.37 151.716c.325 4.548.325 9.097.325 13.645 0 138.72-105.583 298.558-298.558 298.558-59.452 0-114.68-17.219-161.137-47.106 8.447.974 16.568 1.299 25.34 1.299 49.055 0 94.213-16.568 130.274-44.832-46.132-.975-84.792-31.188-98.112-72.772 6.498.974 12.995 1.624 19.818 1.624 9.421 0 18.843-1.3 27.614-3.573-48.081-9.747-84.143-51.98-84.143-102.985v-1.299c13.969 7.797 30.214 12.67 47.431 13.319-28.264-18.843-46.781-51.005-46.781-87.391 0-19.492 5.197-37.36 14.294-52.954 51.655 63.675 129.3 105.258 216.365 109.807-1.624-7.797-2.599-15.918-2.599-24.04 0-57.828 46.782-104.934 104.934-104.934 30.213 0 57.502 12.67 76.67 33.137 23.715-4.548 46.456-13.32 66.599-25.34-7.798 24.366-24.366 44.833-46.132 57.827 21.117-2.273 41.584-8.122 60.426-16.243-14.292 20.791-32.161 39.308-52.628 54.253z"
                ></path>
              </svg>
            </span>
          </a>

          <a class="about-me-box about-me-box3" href="https://discord.com/" aria-label="Discord link placeholder">
            <span class="about-me-icon">
              <svg viewBox="0 0 640 512" xmlns="http://www.w3.org/2000/svg" class="about-me-svg">
                <path
                  d="M524.531,69.836a1.5,1.5,0,0,0-.764-.7A485.065,485.065,0,0,0,404.081,32.03a1.816,1.816,0,0,0-1.923.91,337.461,337.461,0,0,0-14.9,30.6,447.848,447.848,0,0,0-134.426,0,309.541,309.541,0,0,0-15.135-30.6,1.89,1.89,0,0,0-1.924-.91A483.689,483.689,0,0,0,116.085,69.137a1.712,1.712,0,0,0-.788.676C39.068,183.651,18.186,294.69,28.43,404.354a2.016,2.016,0,0,0,.765,1.375A487.666,487.666,0,0,0,176.02,479.918a1.9,1.9,0,0,0,2.063-.676A348.2,348.2,0,0,0,208.12,430.4a1.86,1.86,0,0,0-1.019-2.588,321.173,321.173,0,0,1-45.868-21.853,1.885,1.885,0,0,1-.185-3.126c3.082-2.309,6.166-4.711,9.109-7.137a1.819,1.819,0,0,1,1.9-.256c96.229,43.917,200.41,43.917,295.5,0a1.812,1.812,0,0,1,1.924.233c2.944,2.426,6.027,4.851,9.132,7.16a1.884,1.884,0,0,1-.162,3.126,301.407,301.407,0,0,1-45.89,21.83,1.875,1.875,0,0,0-1,2.611,391.055,391.055,0,0,0,30.014,48.815,1.864,1.864,0,0,0,2.063.7A486.048,486.048,0,0,0,610.7,405.729a1.882,1.882,0,0,0,.765-1.352C623.729,277.594,590.933,167.465,524.531,69.836ZM222.491,337.58c-28.972,0-52.844-26.587-52.844-59.239S193.056,219.1,222.491,219.1c29.665,0,53.306,26.82,52.843,59.239C275.334,310.993,251.924,337.58,222.491,337.58Zm195.38,0c-28.971,0-52.843-26.587-52.843-59.239S388.437,219.1,417.871,219.1c29.667,0,53.307,26.82,52.844,59.239C470.715,310.993,447.538,337.58,417.871,337.58Z"
                ></path>
              </svg>
            </span>
          </a>

          <a class="about-me-box about-me-box4" href="https://example.com/" aria-label="More social links placeholder">
            <span class="about-me-plus">+</span>
          </a>
        </article>
      </div>
    </div>
  </section>

  <section class="h-section section" id="contact">
    <div class="section-frame">
      <div class="section-inner">
        <p class="eyebrow">Contact</p>
        <h2>Book a shoot</h2>
        <p class="hint">Share your info and I’ll reply within 24 hours.</p>
      </div>
      <div class="contact-form-shell">
        <form class="stackedForm">
          <ul class="wrapper">
            <li style="--i:4;">
              <input required placeholder="Name" type="text" class="input" />
            </li>
            <li style="--i:3;">
              <input name="phone" required placeholder="Phone number" class="input" />
            </li>
            <li style="--i:2;">
              <input name="email" required placeholder="E-mail" type="email" class="input" />
            </li>
            <button type="button" style="--i:1;"><span>Submit</span></button>
          </ul>
        </form>
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
    overflow: hidden;
    min-height: 0;
  }

  .hero-grid {
    flex: 1;
    display: grid;
    grid-template-columns: minmax(280px, 1fr) minmax(280px, 1fr) minmax(280px, 1fr);
    gap: 28px;
    align-items: start;
    min-height: 0;
    width: 100%;
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
    flex-wrap: wrap;
  }

  .meta-line {
    color: var(--muted);
    font-size: 14px;
  }

  .cards-stack {
    display: grid;
    grid-template-rows: 1fr 1.1fr;
    gap: 18px;
    min-height: 0;
  }

  .card {
    border-radius: 22px;
    padding: 18px;
    color: #fff;
    box-shadow: 0 18px 50px rgba(0, 0, 0, 0.18);
    position: relative;
    min-height: 180px;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    overflow: hidden;
    min-width: 0;
    backdrop-filter: blur(6px);
  }

  .card.tall {
    min-height: 320px;
  }

  .card.wide {
    min-height: 260px;
    width: 100%;
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
    min-height: 0;
  }

  .selected-grid {
    display: grid;
    grid-template-columns: repeat(2, minmax(140px, 1fr));
    gap: 14px;
    min-width: 0;
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
    width: min(720px, 100%);
  }

  .about-section {
    background: linear-gradient(180deg, #f7fbff 0%, #edf2ff 100%);
  }

  .about-frame {
    justify-content: space-between;
    gap: 20px;
  }

  .about-intro {
    max-width: 760px;
  }

  .about-card-wrap {
    flex: 1;
    min-height: 0;
    width: 100%;
    display: grid;
    place-items: center;
    padding-bottom: 18px;
  }

  .about-me-card {
    position: relative;
    width: min(100%, 560px);
    aspect-ratio: 1 / 1;
    background: #d1d7e3;
    border-radius: 58px;
    overflow: hidden;
    box-shadow: 0 22px 55px rgba(55, 73, 102, 0.28);
    transition: transform 450ms ease;
    isolation: isolate;
  }

  .about-me-background {
    position: absolute;
    inset: 0;
    background: radial-gradient(circle at 95% 108%, #ff89cc 0%, #9cb8ec 30%, #00ffee 62%, #62c2fe 100%);
  }

  .about-me-logo-wrap {
    position: absolute;
    top: 84px;
    right: 24px;
    width: clamp(118px, 26%, 176px);
    aspect-ratio: 3.2 / 1;
    transform: scale(1.04, 0.92) rotate(-4deg);
    transform-origin: right center;
    opacity: 0.84;
    pointer-events: none;
    z-index: 1;
    filter: drop-shadow(0 10px 18px rgba(11, 20, 37, 0.22));
    transition: transform 620ms cubic-bezier(0.22, 1, 0.36, 1), top 620ms cubic-bezier(0.22, 1, 0.36, 1),
      opacity 300ms ease, filter 300ms ease;
  }

  .about-me-logo {
    width: 100%;
    height: 100%;
    object-fit: contain;
    display: block;
  }

  .about-me-photo-wrap {
    position: absolute;
    right: 50%;
    bottom: 50%;
    transform: translate(50%, 50%);
    width: clamp(130px, 26%, 170px);
    aspect-ratio: 1 / 1;
    border-radius: 50%;
    overflow: hidden;
    border: 3px solid rgba(255, 255, 255, 0.86);
    box-shadow: 0 12px 28px rgba(9, 17, 35, 0.35);
    transition: all 600ms ease-in-out;
    z-index: 3;
  }

  .about-me-photo {
    width: 100%;
    height: 100%;
    object-fit: cover;
    display: block;
  }

  .about-me-copy {
    position: absolute;
    top: 20px;
    left: 20px;
    right: 20px;
    z-index: 3;
    padding: 14px 16px;
    background: rgba(12, 17, 26, 0.28);
    border: 1px solid rgba(255, 255, 255, 0.35);
    border-radius: 16px;
    color: #f7fbff;
    backdrop-filter: blur(8px);
  }

  .about-me-label {
    margin: 0 0 6px;
    font-size: 11px;
    letter-spacing: 0.14em;
    text-transform: uppercase;
    font-weight: 700;
    color: rgba(255, 255, 255, 0.88);
  }

  .about-me-snippet {
    margin: 0;
    font-size: clamp(13px, 2vw, 15px);
    line-height: 1.45;
  }

  .about-me-icon {
    display: inline-grid;
    place-items: center;
    width: clamp(42px, 9vw, 62px);
    height: clamp(42px, 9vw, 62px);
  }

  .about-me-svg {
    fill: rgba(255, 255, 255, 0.85);
    width: 100%;
    transition: fill 300ms ease;
  }

  .about-me-box {
    position: absolute;
    padding: 10px;
    text-align: right;
    background: rgba(255, 255, 255, 0.34);
    border-top: 2px solid rgba(255, 255, 255, 0.92);
    border-right: 1px solid rgba(255, 255, 255, 0.95);
    border-radius: 10% 13% 42% 0% / 10% 12% 75% 0%;
    box-shadow: rgba(100, 100, 111, 0.34) -7px 7px 29px 0;
    transform-origin: bottom left;
    transition: all 700ms ease-in-out;
    z-index: 2;
    display: flex;
    justify-content: flex-end;
    align-items: flex-start;
    text-decoration: none;
  }

  .about-me-box::before {
    content: '';
    position: absolute;
    inset: 0;
    border-radius: inherit;
    opacity: 0;
    transition: opacity 350ms ease-in-out;
  }

  .about-me-box:hover .about-me-svg,
  .about-me-box:focus-visible .about-me-svg {
    fill: #fff;
  }

  .about-me-box1 {
    width: 70%;
    height: 70%;
    bottom: -70%;
    left: -70%;
  }

  .about-me-box1::before {
    background: radial-gradient(circle at 30% 107%, #fdf497 0%, #fdf497 8%, #ff53d4 62%, #62c2fe 92%);
  }

  .about-me-box2 {
    width: 50%;
    height: 50%;
    bottom: -50%;
    left: -50%;
    transition-delay: 90ms;
  }

  .about-me-box2::before {
    background: radial-gradient(circle at 30% 107%, #91e9ff 0%, #00acee 90%);
  }

  .about-me-box3 {
    width: 30%;
    height: 30%;
    bottom: -30%;
    left: -30%;
    transition-delay: 180ms;
  }

  .about-me-box3::before {
    background: radial-gradient(circle at 30% 107%, #969fff 0%, #b349ff 90%);
  }

  .about-me-box4 {
    width: 12%;
    height: 12%;
    min-width: 46px;
    min-height: 46px;
    bottom: -12%;
    left: -12%;
    transition-delay: 260ms;
    justify-content: center;
    align-items: center;
  }

  .about-me-plus {
    font-size: 20px;
    line-height: 1;
    font-weight: 700;
    color: rgba(255, 255, 255, 0.84);
  }

  .about-me-box:hover::before,
  .about-me-box:focus-visible::before {
    opacity: 1;
  }

  .about-me-card:hover {
    transform: scale(1.03);
  }

  .about-me-card:hover .about-me-box,
  .about-me-card:focus-within .about-me-box {
    bottom: -1px;
    left: -1px;
  }

  .about-me-card:hover .about-me-logo-wrap,
  .about-me-card:focus-within .about-me-logo-wrap {
    top: calc(50% - 12px);
    transform: scale(1.28, 0.78) rotate(2deg);
    opacity: 1;
    filter: drop-shadow(0 14px 24px rgba(11, 20, 37, 0.32));
  }

  .about-me-card:hover .about-me-photo-wrap,
  .about-me-card:focus-within .about-me-photo-wrap {
    transform: translate(0, 0);
    bottom: 20px;
    right: 20px;
    width: clamp(76px, 16%, 96px);
    border-radius: 20px;
  }

  .about-me-box:focus-visible {
    outline: 2px solid #fff;
    outline-offset: -2px;
  }

  .contact-form-shell {
    display: flex;
    justify-content: center;
    align-items: center;
    width: 100%;
  }

  .stackedForm {
    --form-btn-color-3: linear-gradient(160deg, #9bffd5, #4ac4ff);
    --form-btn-color-2: linear-gradient(160deg, #22d3ee, #6366f1);
    --form-btn-color-1: linear-gradient(160deg, #f97316, #f59e0b);
    --form-btn-base: #111827;
    --form-btn-active-color: #4ac4ff;
    --form-text: #0c111a;
    --form-rotation: rotate3d(0, 1, 0, 180deg);
    --form-text-padding-left: 12px;
    transform: var(--form-rotation);
  }

  .stackedForm .input,
  .stackedForm button {
    width: 240px;
    height: 44px;
    position: relative;
    padding: 10px;
    border: 0.1px solid rgba(255, 255, 255, 0.12);
    border-radius: 10px;
    color: var(--form-text);
    font-weight: 600;
  }

  .stackedForm button {
    background: #0c111a;
    border: none;
    color: #f6f6f6;
  }

  .stackedForm button span {
    display: block;
    transform: var(--form-rotation);
  }

  .stackedForm .wrapper {
    position: relative;
    transform: skew(-14deg, -4deg);
    display: grid;
    gap: 12px;
  }

  .stackedForm .wrapper li,
  .stackedForm button {
    position: relative;
    list-style: none;
    width: 240px;
    z-index: var(--i);
    transition: 0.35s ease;
    color: white;
  }

  .stackedForm .wrapper li::before,
  .stackedForm button::before {
    position: absolute;
    content: '';
    background: #0c111a;
    top: 0;
    left: -36px;
    width: 36px;
    height: 44px;
    transform-origin: right;
    transform: skewY(45deg);
    transition: 0.3s;
    border-radius: 8px 0 0 8px;
  }

  .stackedForm .wrapper li::after,
  .stackedForm button::after {
    position: absolute;
    content: '';
    background: #0c111a;
    width: 240px;
    height: 36px;
    top: -36px;
    left: 0;
    transform-origin: bottom;
    transform: skewX(45deg);
    transition: 0.3s;
    border-radius: 8px 8px 0 0;
  }

  .stackedForm .wrapper li:nth-child(1)::after,
  .stackedForm .wrapper li:nth-child(1)::before {
    background-image: var(--form-btn-color-3);
  }

  .stackedForm .wrapper li:nth-child(2)::after,
  .stackedForm .wrapper li:nth-child(2)::before {
    background-image: var(--form-btn-color-2);
  }

  .stackedForm .wrapper li:nth-child(3)::after,
  .stackedForm .wrapper li:nth-child(3)::before {
    background-image: var(--form-btn-color-1);
  }

  .stackedForm li .input {
    outline: none;
    border: none;
    padding: 0;
    padding-left: var(--form-text-padding-left);
    width: 100%;
    transform: var(--form-rotation);
    color: #0c111a;
    font-weight: 600;
  }

  .stackedForm li .input::placeholder {
    color: rgba(0, 0, 0, 0.55);
  }

  .stackedForm li:nth-child(1) .input {
    background-image: var(--form-btn-color-3);
  }

  .stackedForm li:nth-child(2) .input {
    background-image: var(--form-btn-color-2);
  }

  .stackedForm li:nth-child(3) .input {
    background-image: var(--form-btn-color-1);
  }

  .stackedForm .wrapper li:hover,
  .stackedForm button:hover,
  .stackedForm button:focus {
    transform: translateX(-20px) skew(-14deg, -4deg);
  }

  .stackedForm button:hover,
  .stackedForm button:hover::before,
  .stackedForm button:hover::after,
  .stackedForm button:focus,
  .stackedForm button:focus::before,
  .stackedForm button:focus::after {
    background: var(--form-btn-active-color);
  }

  .stackedForm button:active {
    transform: translateX(0px) skew(-14deg, -4deg);
  }

  @media (max-width: 640px) {
    .stackedForm .input,
    .stackedForm button,
    .stackedForm .wrapper li,
    .stackedForm button::after {
      width: 200px;
    }
    .stackedForm .wrapper li::before {
      left: -32px;
      width: 32px;
    }
    .stackedForm {
      transform: rotate3d(0, 1, 0, 180deg) scale(0.95);
    }
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
    min-width: 0;
  }

  .testimonials-track {
    display: flex;
    gap: 24px;
    padding: 0 24px 20px;
    overflow-x: auto;
    scroll-behavior: smooth;
    -webkit-overflow-scrolling: touch;
    align-items: flex-start;
    min-width: 0;
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
    .about-frame {
      justify-content: flex-start;
    }
    .about-card-wrap {
      align-items: flex-start;
      padding-bottom: 0;
    }
    .about-me-card {
      width: min(100%, 460px);
      border-radius: 42px;
    }
    .about-me-logo-wrap {
      top: 68px;
      width: clamp(108px, 24%, 150px);
    }
    .about-me-card:hover .about-me-logo-wrap,
    .about-me-card:focus-within .about-me-logo-wrap {
      top: calc(50% - 16px);
      transform: scale(1.2, 0.8) rotate(2deg);
    }
  }

  @media (max-width: 640px) {
    .h-section {
      padding: calc(var(--nav-h) + 8px) 16px 16px;
    }
    .hero-grid {
      gap: 20px;
    }
    .hero-actions {
      width: 100%;
    }
    .btn {
      width: 100%;
      justify-content: center;
    }
    .card {
      padding: 16px;
    }
    .card-title {
      font-size: 18px;
    }
    .card-meta {
      font-size: 13px;
    }
    .about-me-card {
      width: min(100%, 360px);
      border-radius: 34px;
    }
    .about-me-logo-wrap {
      top: 58px;
      right: 14px;
      width: 102px;
    }
    .about-me-card:hover .about-me-logo-wrap,
    .about-me-card:focus-within .about-me-logo-wrap {
      top: calc(50% - 18px);
      transform: scale(1.12, 0.84) rotate(2deg);
    }
    .about-me-copy {
      top: 14px;
      left: 14px;
      right: 14px;
      padding: 12px;
    }
    .about-me-snippet {
      font-size: 13px;
    }
    .about-me-box {
      padding: 8px;
    }
    .about-me-box4 {
      min-width: 40px;
      min-height: 40px;
    }
  }
</style>

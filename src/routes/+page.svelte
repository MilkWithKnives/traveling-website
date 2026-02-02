<script lang="ts">
  import { onMount } from 'svelte';

  const navLinks = [
    { label: 'Work', href: '#work' },
    { label: 'Journal', href: '#journal' },
    { label: 'Services', href: '#services' },
    { label: 'Schedule', href: '#schedule' },
    { label: 'About', href: '#about' },
    { label: 'Contact', href: '#contact' }
  ];

  const placeholder = (title: string, subtitle: string, start = '#0ea5e9', end = '#14b8a6') =>
    `data:image/svg+xml;utf8,${encodeURIComponent(
      `<svg xmlns='http://www.w3.org/2000/svg' width='1200' height='1600' viewBox='0 0 1200 1600'><defs><linearGradient id='g' x1='0' y1='0' x2='1' y2='1'><stop stop-color='${start}'/><stop offset='1' stop-color='${end}'/></linearGradient></defs><rect fill='url(#g)' width='1200' height='1600'/><text x='60' y='150' fill='rgba(255,255,255,0.95)' font-family='DM Sans, Arial, sans-serif' font-size='64' font-weight='700'>${title}</text><text x='60' y='230' fill='rgba(255,255,255,0.85)' font-family='DM Sans, Arial, sans-serif' font-size='36'>${subtitle}</text></svg>`
    )}`;

  const portfolio = [
    {
      title: 'Redwood Mist',
      location: 'Redwood National Park, CA',
      year: 2025,
      orientation: 'portrait',
      src: placeholder('Redwood Mist', 'Redwood NP · CA', '#0ea5e9', '#6366f1')
    },
    {
      title: 'Marfa Dustlight',
      location: 'Marfa, TX',
      year: 2025,
      orientation: 'landscape',
      src: placeholder('Marfa Dustlight', 'Marfa · TX', '#f97316', '#f59e0b')
    },
    {
      title: 'Blue Hour Ferry',
      location: 'Seattle, WA',
      year: 2024,
      orientation: 'portrait',
      src: placeholder('Blue Hour Ferry', 'Seattle · WA', '#22d3ee', '#0ea5e9')
    },
    {
      title: 'Zion Narrows',
      location: 'Springdale, UT',
      year: 2024,
      orientation: 'landscape',
      src: placeholder('Zion Narrows', 'Zion · UT', '#10b981', '#65a30d')
    },
    {
      title: 'Brooklyn Rooflines',
      location: 'Brooklyn, NY',
      year: 2023,
      orientation: 'landscape',
      src: placeholder('Brooklyn Rooflines', 'Brooklyn · NY', '#f472b6', '#ec4899')
    },
    {
      title: 'Outer Banks Wind',
      location: 'Hatteras, NC',
      year: 2023,
      orientation: 'portrait',
      src: placeholder('Outer Banks Wind', 'OBX · NC', '#38bdf8', '#0ea5e9')
    }
  ];

  const journal = [
    {
      title: 'Dust, neon, and 35mm in Marfa',
      location: 'West Texas',
      date: 'January 2026',
      summary: 'Sunrise on adobe walls, gas stations at blue hour, and how a 35mm prime handled the wind.',
      tags: ['Editorial', '35mm', 'Road desk'],
      image: placeholder('Marfa Dustlight', 'Journal', '#f97316', '#f59e0b'),
      href: '#'
    },
    {
      title: 'Ferries and fog banks',
      location: 'Puget Sound',
      date: 'December 2025',
      summary: 'Riding the last boat to Bainbridge, testing low-light setups, and why I travel with two bodies.',
      tags: ['Process', 'Pacific Northwest'],
      image: placeholder('Blue Hour Ferry', 'Journal', '#22d3ee', '#0ea5e9'),
      href: '#'
    },
    {
      title: 'Night bus to the redwoods',
      location: 'Northern California',
      date: 'October 2025',
      summary: 'Documenting quiet, towering spaces and the logistics of scouting before first light.',
      tags: ['Scouting', 'Nature'],
      image: placeholder('Redwood Mist', 'Journal', '#0ea5e9', '#6366f1'),
      href: '#'
    }
  ];

  const services = [
    {
      title: 'Editorial assignments',
      desc: 'Magazine-style travel features, hospitality stories, and brand narratives built on location scouting and sequencing.'
    },
    {
      title: 'Elopements & weddings',
      desc: 'Documentary coverage across the U.S. with cinematic portraits; passport ready for international couples.'
    },
    {
      title: 'Adventure Portraits',
      desc: 'Solo or couple sessions in dramatic landscapes—permits, sunrise calls, and backup plans handled.'
    }
  ];

  const schedule = [
    { month: 'March 2026', place: 'Southwest loop · AZ & UT deserts', slots: 3 },
    { month: 'April 2026', place: 'Pacific Northwest · Seattle / Portland', slots: 2 },
    { month: 'May 2026', place: 'New York & Hudson Valley', slots: 2 },
    { month: 'June 2026', place: 'Maine coast & Acadia', slots: 3 }
  ];

  const testimonials = [
    {
      quote:
        'He plans like a producer and shoots like a poet. Our brand launch felt cinematic yet honest.',
      name: 'Camila Duarte',
      role: 'CMO, Azulejo Hotels'
    },
    {
      quote:
        'We hiked in the dark to catch first light. The images feel like the trip—windy, real, unforgettable.',
      name: 'Ethan & Mara',
      role: 'Adventure elopement, Faroe Islands'
    }
  ];

  let isLight = false;
  let track: HTMLDivElement | null = null;

  const scrollToSection = (hash: string) => {
    const id = hash.replace('#', '');
    const el = document.getElementById(id);
    if (el && track) {
      const left = el.offsetLeft - track.offsetLeft;
      track.scrollTo({ left, behavior: 'smooth' });
    }
  };

  const setTheme = (mode: 'light' | 'dark') => {
    isLight = mode === 'light';
    if (typeof document !== 'undefined') {
      document.documentElement.dataset.theme = mode;
      localStorage.setItem('theme', mode);
    }
  };

  const handleThemeToggle = (event: Event) => {
    const target = event.currentTarget as HTMLInputElement;
    setTheme(target.checked ? 'light' : 'dark');
  };

  onMount(() => {
    const saved = localStorage.getItem('theme');
    setTheme(saved === 'light' ? 'light' : 'dark');

    const onWheel = (event: WheelEvent) => {
      if (!track) return;
      const horizontal = Math.abs(event.deltaX) >= Math.abs(event.deltaY);
      if (!horizontal) {
        event.preventDefault();
        track.scrollLeft += event.deltaY;
      }
    };

    window.addEventListener('wheel', onWheel, { passive: false });

    return () => {
      window.removeEventListener('wheel', onWheel);
    };
  });
</script>

  <svelte:head>
  <title>Full Scope Media LLC | Ryan Champion | Editorial travel stories across the U.S.</title>
  <meta
    name="description"
    content="Ryan Champion of Full Scope Media LLC is a U.S.-based traveling photographer crafting editorial stories for couples, brands, and publications—passport ready for international commissions."
  />
</svelte:head>

<div class="page">
  <header class="nav">
    <div class="logo">Full Scope Media</div>
    <nav>
      {#each navLinks as link}
        <a
          href={link.href}
          on:click|preventDefault={() => {
            scrollToSection(link.href);
          }}
          >{link.label}</a
        >
      {/each}
    </nav>
    <div class="theme-toggle">
      <label class="switch" aria-label="Toggle light mode">
        <input id="theme-toggle" type="checkbox" bind:checked={isLight} on:change={handleThemeToggle} />
        <span class="slider">
          <div class="star star_1"></div>
          <div class="star star_2"></div>
          <div class="star star_3"></div>
          <svg viewBox="0 0 16 16" class="cloud_1 cloud" aria-hidden="true">
            <path
              transform="matrix(.77976 0 0 .78395-299.99-418.63)"
              fill="#fff"
              d="m391.84 540.91c-.421-.329-.949-.524-1.523-.524-1.351 0-2.451 1.084-2.485 2.435-1.395.526-2.388 1.88-2.388 3.466 0 1.874 1.385 3.423 3.182 3.667v.034h12.73v-.006c1.775-.104 3.182-1.584 3.182-3.395 0-1.747-1.309-3.186-2.994-3.379.007-.106.011-.214.011-.322 0-2.707-2.271-4.901-5.072-4.901-2.073 0-3.856 1.202-4.643 2.925"
            ></path>
          </svg>
        </span>
      </label>
      <a
        class="cta"
        href="#contact"
        on:click|preventDefault={() => {
          scrollToSection('#contact');
        }}>Book</a
      >
    </div>
  </header>

  <div class="scroll-track" bind:this={track}>
    <section class="hero panel">
    <div class="hero__text">
      <p class="eyebrow">Ryan Champion · Full Scope Media LLC · Road desk USA</p>
      <h1>Editorial stories from the American road—passport ready.</h1>
      <p class="lede">
        Documentary-first imagery with cinematic framing for couples, brands, and publications. Currently traveling the
        United States, booking international work with notice.
      </p>
      <div class="hero__actions">
        <a class="btn primary" href="#work">See work</a>
        <a class="btn ghost" href="#journal">Read the journal</a>
      </div>
      <div class="hero__meta">
        <span>Now: Southwest (Jan–Mar 2026)</span>
        <span>Next: PNW, NYC</span>
        <span>International on request</span>
      </div>
    </div>
    <div class="hero__grid">
      {#each portfolio.slice(0, 3) as shot}
        <figure class={shot.orientation}>
          <img src={shot.src} alt={`${shot.title} in ${shot.location}`} loading="lazy" />
          <figcaption>
            <span>{shot.location}</span>
            <span>{shot.year}</span>
          </figcaption>
        </figure>
      {/each}
    </div>
  </section>

  <section id="work" class="section work panel">
    <div class="section__heading">
      <p class="eyebrow">Selected work</p>
      <h2>Travel chapters</h2>
      <p class="hint">Curated galleries from recent journeys.</p>
    </div>
    <div class="masonry">
      {#each portfolio as shot}
        <figure class={shot.orientation}>
          <img src={shot.src} alt={`${shot.title} in ${shot.location}`} loading="lazy" />
          <figcaption>
            <div>
              <span class="title">{shot.title}</span>
              <span class="meta">{shot.location}</span>
            </div>
            <span class="year">{shot.year}</span>
          </figcaption>
        </figure>
      {/each}
    </div>
  </section>

  <section id="journal" class="section journal panel">
    <div class="section__heading">
      <p class="eyebrow">Field notes</p>
      <h2>Journal</h2>
      <p class="hint">Dispatches from the road—process, places, and people.</p>
    </div>
    <div class="journal__grid">
      {#each journal as post}
        <article>
          <div class="thumb">
            <img src={post.image} alt={post.title} loading="lazy" />
          </div>
          <div class="meta">
            <span>{post.location}</span>
            <span>·</span>
            <span>{post.date}</span>
          </div>
          <h3>{post.title}</h3>
          <p class="summary">{post.summary}</p>
          <div class="tags">
            {#each post.tags as tag}
              <span class="pill">{tag}</span>
            {/each}
          </div>
          <a class="text-link" href={post.href}>Open story →</a>
        </article>
      {/each}
    </div>
  </section>

  <section id="services" class="section services panel">
    <div class="section__heading">
      <p class="eyebrow">Offerings</p>
      <h2>Built for travel</h2>
      <p class="hint">Lean production, location-ready, story-obsessed.</p>
    </div>
    <div class="cards">
      {#each services as service}
        <article>
          <h3>{service.title}</h3>
          <p>{service.desc}</p>
        </article>
      {/each}
    </div>
  </section>

  <section id="schedule" class="section schedule panel">
    <div class="section__heading">
      <p class="eyebrow">Travel calendar</p>
      <h2>Where I’ll be</h2>
      <p class="hint">Hold a date across the U.S. or request an international stop.</p>
    </div>
    <div class="schedule__list">
      {#each schedule as stop}
        <div class="row">
          <div>
            <p class="month">{stop.month}</p>
            <p class="place">{stop.place}</p>
          </div>
          <p class="slots">{stop.slots} open slots</p>
        </div>
      {/each}
    </div>
  </section>

  <section id="about" class="section about panel">
    <div class="about__photo">
      <img
        src={placeholder('Ryan Champion', 'Full Scope Media · USA', '#f472b6', '#8b5cf6')}
        alt="Portrait placeholder of Ryan Champion"
        loading="lazy"
      />
    </div>
    <div class="about__text">
      <p class="eyebrow">Behind the lens</p>
      <h2>Ryan Champion — Full Scope Media LLC</h2>
      <p>
        I’m Ryan Champion, a traveling photographer writing visual essays from the American road under Full Scope Media.
        The work stays documentary-first with editorial pacing—planning like a producer, shooting like a storyteller,
        and delivering images that feel like the trip itself.
      </p>
      <ul>
        <li>U.S.-based and on the road most months; international commissions with notice</li>
        <li>Dual bodies with fast primes; drones where permitted</li>
        <li>Delivery: 72h selects, full galleries in 3 weeks</li>
        <li>Pronouns: he/him</li>
      </ul>
    </div>
  </section>

  <section class="section testimonials panel">
    <div class="section__heading">
      <p class="eyebrow">Kind words</p>
      <h2>Trusted by couples & brands</h2>
    </div>
    <div class="testimonials__grid">
      {#each testimonials as item}
        <blockquote>
          <p>“{item.quote}”</p>
          <footer>
            <span class="name">{item.name}</span>
            <span class="role">{item.role}</span>
          </footer>
        </blockquote>
      {/each}
    </div>
  </section>

  <section id="contact" class="section contact panel">
    <div>
      <p class="eyebrow">Let’s plan</p>
      <h2>Tell me your destination</h2>
      <p class="hint">Currently crossing the U.S.; open to international work with travel notice.</p>
    </div>
    <form class="contact__form">
      <div class="grid">
        <label>
          Name
          <input name="name" placeholder="Your full name" />
        </label>
        <label>
          Email
          <input type="email" name="email" placeholder="you@example.com" />
        </label>
        <label>
          Location
          <input name="location" placeholder="City / region" />
        </label>
        <label>
          Dates
          <input name="dates" placeholder="e.g. June 4–8, 2026" />
        </label>
      </div>
      <label>
        Project details
        <textarea name="details" rows="4" placeholder="What are we shooting? What matters most?"></textarea>
      </label>
      <button type="button" class="btn primary">Send inquiry</button>
      <p class="small">Prefer email? Drop a note at hello@fullscopemedia.com</p>
    </form>
  </section>

  <footer class="footer panel">
    <div class="logo">Full Scope Media</div>
    <div class="footer__links">
      <a href="https://instagram.com" rel="noreferrer">Instagram</a>
      <a href="https://vsco.co" rel="noreferrer">VSCO</a>
      <a href="mailto:hello@fullscopemedia.com">Email</a>
    </div>
    <p class="small">On the road across the U.S. · Passport ready</p>
  </footer>
</div>
</div>

<style>
  :global(:root) {
    --bg: #0e0f13;
    --page-bg: radial-gradient(circle at 20% 20%, rgba(255, 255, 255, 0.1), transparent 35%),
      radial-gradient(circle at 80% 0%, rgba(255, 255, 255, 0.08), transparent 30%), #0e0f13;
    --nav-height: 72px;
    --text: #f6f6f6;
    --subtext: #cfd0d6;
    --muted: #9aa0ad;
    --border: rgba(255, 255, 255, 0.08);
    --card: rgba(255, 255, 255, 0.02);
    --card-strong: rgba(0, 0, 0, 0.35);
    --pill: rgba(255, 255, 255, 0.06);
    --shadow: rgba(0, 0, 0, 0.3);
    --accent1: #9bffd5;
    --accent2: #4ac4ff;
    --btn-ghost: rgba(255, 255, 255, 0.06);
    --input-bg: rgba(0, 0, 0, 0.35);
    color-scheme: dark;
  }

  :global(:root[data-theme='light']) {
    --bg: #f7f7fb;
    --page-bg: radial-gradient(circle at 20% 20%, rgba(14, 17, 26, 0.06), transparent 36%),
      radial-gradient(circle at 80% 0%, rgba(14, 17, 26, 0.05), transparent 30%), #f7f7fb;
    --text: #0c111a;
    --subtext: #3a3f4a;
    --muted: #5c6470;
    --border: rgba(12, 17, 26, 0.08);
    --card: rgba(255, 255, 255, 0.82);
    --card-strong: rgba(255, 255, 255, 0.9);
    --pill: rgba(12, 17, 26, 0.06);
    --shadow: rgba(0, 0, 0, 0.12);
    --accent1: #0ea5e9;
    --accent2: #10b981;
    --btn-ghost: rgba(12, 17, 26, 0.06);
    --input-bg: rgba(255, 255, 255, 0.86);
    color-scheme: light;
  }

  :global(body) {
    margin: 0;
    font-family: 'DM Sans', 'Helvetica Neue', Arial, sans-serif;
    background: var(--page-bg);
    color: var(--text);
    transition: background 0.45s ease, color 0.45s ease;
    overflow: hidden;
  }

  :global(html) {
    scroll-behavior: smooth;
  }

  :global(a) {
    color: inherit;
    text-decoration: none;
  }

  :global(img) {
    display: block;
    width: 100%;
    height: auto;
    border-radius: 18px;
    object-fit: cover;
  }

  .page {
    height: 100vh;
    padding: 16px clamp(14px, 4vw, 56px) 16px;
    display: flex;
    flex-direction: column;
    gap: 12px;
    overflow: hidden;
  }

  .scroll-track {
    display: flex;
    flex-direction: row;
    align-items: stretch;
    gap: 56px;
    overflow-x: auto;
    overflow-y: hidden;
    padding: 8px 0 12px;
    overscroll-behavior-x: contain;
  }

  .panel {
    flex: 0 0 min(90vw, 1100px);
    width: min(90vw, 1100px);
    min-height: calc(100vh - var(--nav-height) - 40px);
    overflow: hidden;
    padding-bottom: 12px;
  }

  .scroll-track::-webkit-scrollbar {
    height: 10px;
  }

  .scroll-track::-webkit-scrollbar-thumb {
    background: color-mix(in srgb, var(--border) 100%, transparent);
    border-radius: 999px;
  }

  .nav {
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 24px;
    flex-wrap: wrap;
    position: sticky;
    top: 0;
    padding: 18px 22px;
    background: color-mix(in srgb, var(--bg) 92%, transparent);
    backdrop-filter: blur(12px);
    border: 1px solid var(--border);
    border-radius: 16px;
    z-index: 10;
    animation: floatUp 0.7s ease both;
  }

  .logo {
    font-weight: 700;
    letter-spacing: 0.08em;
    text-transform: uppercase;
  }

  nav {
    display: flex;
    gap: 18px;
    font-size: 15px;
  }

  nav a {
    opacity: 0.78;
  }

  nav a:hover {
    opacity: 1;
  }

  .theme-toggle {
    display: inline-flex;
    align-items: center;
    gap: 8px;
  }

  .switch {
    font-size: 17px;
    position: relative;
    display: inline-block;
    width: 4em;
    height: 2.2em;
    border-radius: 30px;
    box-shadow: 0 0 10px color-mix(in srgb, var(--shadow) 35%, transparent);
  }

  .switch input {
    opacity: 0;
    width: 0;
    height: 0;
  }

  .slider {
    position: absolute;
    cursor: pointer;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    background-color: #2a2a2a;
    transition: 0.4s;
    border-radius: 30px;
    overflow: hidden;
  }

  :root[data-theme='light'] .slider {
    background-color: #e2e8f0;
  }

  .slider:before {
    position: absolute;
    content: '';
    height: 1.2em;
    width: 1.2em;
    border-radius: 20px;
    left: 0.5em;
    bottom: 0.5em;
    transition: 0.4s;
    transition-timing-function: cubic-bezier(0.81, -0.04, 0.38, 1.5);
    box-shadow: inset 8px -4px 0px 0px #fff;
  }

  .switch input:checked + .slider {
    background-color: #00a6ff;
  }

  :root[data-theme='light'] .switch input:checked + .slider {
    background-color: #0ea5e9;
  }

  .switch input:checked + .slider:before {
    transform: translateX(1.8em);
    box-shadow: inset 15px -4px 0px 15px #ffcf48;
  }

  .star {
    background-color: #fff;
    border-radius: 50%;
    position: absolute;
    width: 5px;
    transition: all 0.4s;
    height: 5px;
  }

  .star_1 {
    left: 2.5em;
    top: 0.5em;
  }

  .star_2 {
    left: 2.2em;
    top: 1.2em;
  }

  .star_3 {
    left: 3em;
    top: 0.9em;
  }

  .switch input:checked ~ .slider .star {
    opacity: 0;
  }

  .cloud {
    width: 3.5em;
    position: absolute;
    bottom: -1.4em;
    left: -1.1em;
    opacity: 0;
    transition: all 0.4s;
  }

  .switch input:checked ~ .slider .cloud {
    opacity: 1;
  }

  .cta {
    padding: 10px 16px;
    border-radius: 999px;
    border: 1px solid color-mix(in srgb, var(--border) 100%, transparent);
    font-size: 14px;
  }

  .hero {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
    gap: 32px;
    align-items: center;
    animation: floatUp 0.9s ease 0.05s both;
    min-height: calc(100vh - var(--nav-height) - 120px);
  }

  .hero__text h1 {
    font-size: clamp(32px, 5vw, 56px);
    line-height: 1.05;
    margin: 10px 0 16px;
  }

  .hero__text .lede {
    max-width: 560px;
    font-size: 18px;
    color: var(--subtext);
  }

  .hero__actions {
    display: flex;
    gap: 12px;
    margin: 20px 0;
  }

  .hero__meta {
    display: flex;
    gap: 12px;
    flex-wrap: wrap;
    color: var(--muted);
    font-size: 14px;
  }

  .hero__grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(180px, 1fr));
    gap: 16px;
  }

  figure {
    position: relative;
    overflow: hidden;
    background: linear-gradient(135deg, rgba(255, 255, 255, 0.04), rgba(255, 255, 255, 0.01));
    border-radius: 18px;
    transition: transform 0.45s ease, box-shadow 0.45s ease;
    animation: floatUp 0.9s ease both;
  }

  figcaption {
    position: absolute;
    left: 12px;
    right: 12px;
    bottom: 12px;
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 10px 12px;
    border-radius: 12px;
    background: var(--card-strong);
    backdrop-filter: blur(8px);
    font-size: 13px;
    color: var(--text);
  }

  figcaption .title {
    display: block;
    font-weight: 600;
  }

  figcaption .meta,
  figcaption .year {
    color: var(--subtext);
  }

  .portrait {
    grid-row: span 2;
  }

  .landscape {
    grid-column: span 2;
  }

  .section {
    display: grid;
    gap: 24px;
    animation: floatUp 0.9s ease 0.1s both;
  }

  .section__heading h2 {
    margin: 6px 0;
    font-size: 32px;
  }

  .eyebrow {
    font-size: 13px;
    letter-spacing: 0.12em;
    text-transform: uppercase;
    color: var(--muted);
  }

  .hint {
    color: var(--subtext);
  }

  .masonry {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
    gap: 16px;
  }

  .masonry figure {
    min-height: 240px;
    animation-delay: calc(0.05s * var(--i, 1));
  }

  .services .cards {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
    gap: 16px;
  }

  .services article {
    padding: 18px;
    border: 1px solid var(--border);
    border-radius: 14px;
    background: var(--card);
    transition: transform 0.35s ease, border-color 0.35s ease, box-shadow 0.35s ease;
  }

  .services h3 {
    margin: 0 0 10px;
    font-size: 18px;
  }

  .journal__grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
    gap: 16px;
  }

  .journal article {
    display: grid;
    gap: 10px;
    padding: 14px;
    border-radius: 14px;
    border: 1px solid var(--border);
    background: var(--card);
    transition: transform 0.35s ease, border-color 0.35s ease, box-shadow 0.35s ease;
  }

  .journal .thumb img {
    height: 160px;
    object-fit: cover;
  }

  .journal .meta {
    display: flex;
    gap: 8px;
    color: var(--muted);
    font-size: 13px;
    align-items: center;
  }

  .journal h3 {
    margin: 0;
    font-size: 18px;
  }

  .journal .summary {
    margin: 0;
    color: var(--subtext);
    font-size: 15px;
  }

  .tags {
    display: flex;
    flex-wrap: wrap;
    gap: 8px;
  }

  .pill {
    padding: 6px 10px;
    border-radius: 999px;
    background: var(--pill);
    border: 1px solid var(--border);
    font-size: 12px;
    color: var(--text);
  }

  .text-link {
    color: var(--accent1);
    font-weight: 600;
    font-size: 14px;
  }

  .schedule__list {
    display: grid;
    gap: 12px;
  }

  .schedule .row {
    padding: 16px;
    border-radius: 12px;
    border: 1px solid var(--border);
    background: var(--card);
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 12px;
    flex-wrap: wrap;
    transition: transform 0.35s ease, border-color 0.35s ease, box-shadow 0.35s ease;
  }

  .schedule .month {
    margin: 0;
    font-weight: 600;
  }

  .schedule .place {
    margin: 4px 0 0;
    color: var(--subtext);
  }

  .schedule .slots {
    margin: 0;
    color: #9ee6c3;
    font-weight: 600;
  }

  .about {
    grid-template-columns: repeat(auto-fit, minmax(260px, 1fr));
    align-items: center;
    gap: 32px;
  }

  .about__photo img {
    border-radius: 18px;
  }

  .about__text h2 {
    margin: 8px 0 12px;
  }

  .about__text ul {
    list-style: none;
    padding: 0;
    margin: 16px 0 0;
    color: var(--subtext);
    display: grid;
    gap: 6px;
  }

  .testimonials__grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
    gap: 14px;
  }

  blockquote {
    margin: 0;
    padding: 18px;
    border-radius: 14px;
    border: 1px solid var(--border);
    background: var(--card);
  }

  blockquote p {
    margin: 0 0 10px;
    font-size: 16px;
  }

  blockquote .name {
    font-weight: 600;
  }

  blockquote .role {
    color: var(--subtext);
    margin-left: 8px;
  }

  .contact {
    grid-template-columns: repeat(auto-fit, minmax(260px, 1fr));
    gap: 24px;
    align-items: start;
  }

  .contact__form {
    padding: 18px;
    border-radius: 14px;
    border: 1px solid var(--border);
    background: var(--card);
    display: grid;
    gap: 12px;
    animation: floatUp 0.9s ease 0.12s both;
  }

  .contact__form label {
    display: grid;
    gap: 6px;
    font-size: 14px;
    color: var(--subtext);
  }

  .contact__form input,
  .contact__form textarea {
    width: 100%;
    padding: 12px;
    border-radius: 10px;
    border: 1px solid var(--border);
    background: var(--input-bg);
    color: var(--text);
  }

  .contact__form input::placeholder,
  .contact__form textarea::placeholder {
    color: var(--muted);
  }

  .contact__form .grid {
    display: grid;
    gap: 10px;
    grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  }

  .btn {
    display: inline-flex;
    align-items: center;
    justify-content: center;
    gap: 6px;
    padding: 12px 16px;
    border-radius: 999px;
    font-weight: 600;
    border: 1px solid color-mix(in srgb, var(--border) 100%, transparent);
    cursor: pointer;
    transition: transform 160ms ease, box-shadow 160ms ease, background 160ms ease;
  }

  .btn.primary {
    background: linear-gradient(120deg, var(--accent1), var(--accent2));
    color: #0c111a;
    border: none;
    box-shadow: 0 12px 40px color-mix(in srgb, var(--accent2) 45%, transparent);
  }

  .btn.ghost {
    background: var(--btn-ghost);
    color: var(--text);
  }

  .btn:hover {
    transform: translateY(-2px);
  }

  .small {
    color: var(--muted);
    font-size: 13px;
    margin: 0;
  }

  .footer {
    display: flex;
    flex-wrap: wrap;
    gap: 12px;
    align-items: center;
    justify-content: space-between;
    border-top: 1px solid var(--border);
    padding-top: 18px;
    margin-top: 12px;
    animation: floatUp 0.8s ease both;
  }

  .footer__links {
    display: flex;
    gap: 12px;
  }

  @media (max-width: 700px) {
    .nav {
      position: static;
    }

    .hero__grid {
      grid-template-columns: repeat(auto-fit, minmax(140px, 1fr));
    }

    .landscape {
      grid-column: span 1;
    }
  }

  figure:hover img {
    transform: scale(1.04);
    filter: saturate(1.05);
  }

  figure:hover {
    transform: translateY(-4px);
    box-shadow: 0 18px 40px var(--shadow);
  }

  .services article:hover,
  .journal article:hover,
  .schedule .row:hover {
    transform: translateY(-4px);
    border-color: color-mix(in srgb, var(--border) 100%, transparent);
    box-shadow: 0 18px 40px var(--shadow);
  }

  @keyframes floatUp {
    0% {
      opacity: 0;
      transform: translateY(24px) scale(0.98);
    }
    100% {
      opacity: 1;
      transform: translateY(0) scale(1);
    }
  }

  @media (prefers-reduced-motion: reduce) {
    * {
      animation-duration: 0.001ms !important;
      animation-iteration-count: 1 !important;
      transition-duration: 0.001ms !important;
    }
    :global(html) {
      scroll-behavior: auto;
    }
  }
</style>

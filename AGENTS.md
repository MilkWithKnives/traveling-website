# Repository Guidelines

## Project Structure & Module Organization

- SvelteKit layout is assumed: place pages in `src/routes` (e.g., `src/routes/+page.svelte` for the landing gallery, `src/routes/journal/+page.svelte` for travel notes). Reusable UI, stores, and utilities belong in `src/lib` with folders like `components/`, `styles/`, and `utils/`.
- Public assets (photos, favicons, robots.txt) live in `static/`; serve images from `static/photos/<year>/<location>/<slug>.{webp,jpg}`. Keep originals outside the repo; commit only web-friendly exports.
- If you add API endpoints (contact form, EXIF feeds), place them in `src/routes/api/*/+server.ts`.

## Build, Test, and Development Commands

- `npm install` — set up dependencies after scaffolding with `npm create svelte@latest`.
- `npm run dev -- --open` — start the local dev server with hot reload.
- `npm run check` — SvelteKit sync + type and accessibility checks.
- `npm run lint` — ESLint/Prettier (if configured) for style conformance.
- `npm run test` — Vitest + Testing Library unit/UI tests (add soon).
- `npm run build` / `npm run preview` — production build and local preview of the built site.

## Coding Style & Naming Conventions

- Use TypeScript and 2-space indentation. Components in PascalCase (`HeroGrid.svelte`); routes in kebab-case (`road-notes`).
- Favor `src/lib` alias imports (`import Card from '$lib/components/Card.svelte';`).
- Keep CSS modular: component-scoped styles first; shared tokens in `src/lib/styles/tokens.css` (colors, spacing). Target fast page loads: prefer CSS grid/flex over heavy libraries.
- Image discipline: export WebP first; cap hero images ~200–300 KB; include descriptive `alt` text.

## Testing Guidelines

- Write unit/component tests with Vitest + `@testing-library/svelte` in `src/lib/**/__tests__` or `tests/`. Mirror file names (`GalleryGrid.test.ts` for `GalleryGrid.svelte`).
- Stub network calls and file reads; do not rely on live APIs. Add at least one accessibility assertion per component (landmarks, alt text, keyboard focus).

## Commit & Pull Request Guidelines

- Commits: use Conventional Commit prefixes (`feat:`, `fix:`, `chore:`, `docs:`, `test:`, `refactor:`). Aim for focused changes and present-tense summaries.
- Branches: `feature/<short-desc>` or `fix/<short-desc>`.
- PRs: include a short intent, before/after screenshots (desktop + mobile), steps to test (`npm run dev` / `npm run preview`), and mention any performance or accessibility impacts. Link related issues or trip stops when relevant.

## Content, Security, and Config

- Never commit secrets or map/photo service API keys; keep them in `.env` with `VITE_` prefixes only when safe for the client. Add `.env.example` placeholders.
- If using geotagged photos, strip precise GPS before publishing or blur sensitive locations. Provide credit/attribution when required.

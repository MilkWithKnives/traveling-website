import { writable } from 'svelte/store';

export const activeIndex = writable(0);

export type ScrollerHandle = {
	scrollToIndex: (i: number, behavior?: ScrollBehavior) => void;
};

export const scrollerHandle = writable<ScrollerHandle | null>(null);

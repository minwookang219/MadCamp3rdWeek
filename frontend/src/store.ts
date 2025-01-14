import { writable } from 'svelte/store';

export const resultImageStore = writable<string | null>(null);
export const characterImageStore = writable<string | null>(null);

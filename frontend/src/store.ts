import { writable } from 'svelte/store';

export const resultImageStore = writable<string | null>(null);

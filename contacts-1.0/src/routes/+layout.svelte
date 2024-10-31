<script lang="ts">
	import '../app.postcss';
	import { computePosition, autoUpdate, offset, shift, flip, arrow } from '@floating-ui/dom';
	import { AppShell, AppBar } from '@skeletonlabs/skeleton';
	import { popup } from '@skeletonlabs/skeleton';
	import type { PopupSettings } from '@skeletonlabs/skeleton';
	// @ts-ignore
	import Navigation from '$lib/Navigation/Navigation.svelte';
	// Highlight JS
	import hljs from 'highlight.js/lib/core';
	import 'highlight.js/styles/github-dark.css';
	import { storeHighlightJs } from '@skeletonlabs/skeleton';
	// @ts-ignore
	// @ts-ignore
	import xml from 'highlight.js/lib/languages/xml'; // for HTML
	// @ts-ignore
	// @ts-ignore
	import css from 'highlight.js/lib/languages/css';
	// @ts-ignore
	// @ts-ignore
	import javascript from 'highlight.js/lib/languages/javascript';
	// @ts-ignore
	// @ts-ignore
	import { Avatar } from '@skeletonlabs/skeleton';
	import typescript from 'highlight.js/lib/languages/typescript';
	import { initializeStores, Drawer, getDrawerStore } from '@skeletonlabs/skeleton';
	hljs.registerLanguage('xml', xml); // for HTML
	hljs.registerLanguage('css', css);
	hljs.registerLanguage('javascript', javascript);
	hljs.registerLanguage('typescript', typescript);
	storeHighlightJs.set(hljs);
	import Icon from '@iconify/svelte';
	// Floating UI for Popups

	import { storePopup } from '@skeletonlabs/skeleton';
	storePopup.set({ computePosition, autoUpdate, offset, shift, flip, arrow });

	initializeStores();

	const drawerStore = getDrawerStore();
	function drawerOpen() {
		drawerStore.open({});
	}

	const popupFeatured: PopupSettings = {
		// Represents the type of event that opens/closed the popup
		event: 'click',
		// Matches the data-popup value on your popup element
		target: 'popupFeatured',
		// Defines which side of your trigger the popup will appear
		placement: 'bottom'
	};

	const popupHover: PopupSettings = {
		event: 'hover',
		target: 'popupHover',
		placement: 'top'
	};
</script>

<!-- App Shell -->
<Drawer width="w-64 p-4">
	<h2 class="py-4 px-5">Contacts</h2>
	<hr />
	<Navigation />
</Drawer>
<AppShell slotSidebarLeft="bg-surface-500/5 w-0 lg:w-64 ">
	<svelte:fragment slot="header">
		<!-- App Bar -->
		<AppBar padding="px-0 py-1" gap="1">
			<svelte:fragment slot="lead">
				<div class="flex items-center w-64 px-0">
					<button class="lg:hidden btn btn-sm mr-4" on:click={drawerOpen}>
						<span>
							<svg viewBox="0 0 100 80" class="fill-token w-4 h-4">
								<rect width="100" height="20" />
								<rect y="30" width="100" height="20" />
								<rect y="60" width="100" height="20" />
							</svg>
						</span>
					</button>
					<div class="flex flex-row gap-2 pl-7">
						<Icon icon="material-symbols:contacts-product" class="w-7 h-7 text-surface-200"  />
					<strong class="text-base uppercase text-surface-200 ">Contacts</strong>
					</div>
					
				</div>
			</svelte:fragment>

			<div
				class="input-group input-group-divider w-4/5 rounded-xl grid-cols-[auto_1fr_auto] focus-within:shadow-md visible:shadow-white"
			>
				<div class="input-group-shim">
					<label for="search">
						<Icon icon="material-symbols:search" width="20px" height="20px" />
					</label>
				</div>
				<input type="search" id="search" placeholder="Search..." class="w-5/6 p-2" />
				<button class="variant-ghost-surface rounded-md">Submit</button>
			</div>

			<svelte:fragment slot="trail">
				<div class="w-28 p-2">
					<div use:popup={popupFeatured}>
						<!-- <Avatar
							border="border-4 border-surface-300-600-token hover:!border-primary-500"
							cursor="cursor-pointer"
							width="w-10"
						/>
					</div> -->
					<div class="">
						<img  class="cursor-pointer object-fill w-10 placeholder-circle" src="https://images.unsplash.com/photo-1617296538902-887900d9b592?ixid=M3w0Njc5ODF8MHwxfGFsbHx8fHx8fHx8fDE2ODc5NzExMDB8&ixlib=rb-4.0.3&w=128&h=128&auto=format&fit=crop" alt="">
				</div>
					<div class="card px-4 w-[420px] h-auto py-8  pb-9 shadow-xl" data-popup="popupFeatured">
						<div class="flex flex-col items-center justify-center gap-4">
							<div class="font-medium text-gray-300">test@gmail.com</div>
							<div class="">
								<img class=" object-fill w-20 placeholder-circle" src="https://images.unsplash.com/photo-1617296538902-887900d9b592?ixid=M3w0Njc5ODF8MHwxfGFsbHx8fHx8fHx8fDE2ODc5NzExMDB8&ixlib=rb-4.0.3&w=128&h=128&auto=format&fit=crop" alt="">
						</div>
						<div class="font-medium text-gray-300">Hi Test User</div>

							<div><button type="button" class="btn variant-outline-primary">Manage your Google Account</button></div>
						</div>
						
					</div>
				</div>
			</svelte:fragment>
		</AppBar>
	</svelte:fragment>
	<svelte:fragment slot="sidebarLeft">
		<Navigation />
	</svelte:fragment>

	<!-- Page Route Content -->
	<slot />
</AppShell>

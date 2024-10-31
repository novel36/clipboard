<script lang="ts">
	import Contactbox from '$lib/components/contacts/contactbox.svelte';
import Icon from '@iconify/svelte';
	import { getDrawerStore, popup, type PopupSettings } from '@skeletonlabs/skeleton';
	import {  Dropdown, DropdownItem } from 'flowbite-svelte';
	let toggle = false;
	let isDropdownOpen = false;

	const drawerStore = getDrawerStore();

	// const popupHover: PopupSettings = {
	// 	event: 'hover',
	// 	target: 'popupHover',
	// 	placement: 'bottom'
	// };
	const printPopupHover: PopupSettings = {
		event: 'hover',
		target: 'printPopupHover',
		placement: 'bottom'
	};
	const exportPopupHover: PopupSettings = {
		event: 'hover',
		target: 'exportPopupHover',
		placement: 'bottom'
	};
	function toggleDropdown() {
		toggle = !isDropdownOpen ? true : false;
	}
</script>

<div class="card p-2 variant-filled-primary" data-popup="printPopupHover">
	<p class="text-xs">print contacts</p>
	<div class="arrow variant-filled-primary" />
</div>

<div class="card p-2 variant-filled-primary" data-popup="exportPopupHover">
	<p class="text-xs">export contacts</p>
	<div class="arrow variant-filled-primary" />
</div>

<div class=" h-full flex flex-col w-full px-2 mt-4 gap-3">
	<div class="h-16 px-2 w-full flex items-center">
		<h1 class="text-2xl font-bold">contacts</h1>
	</div>
	<div class="table-container">
		<!-- Native Table Element -->
		<table class="table table-hover">
			<thead>
				<tr>
					<th>Name</th>
					<th>Phone number</th>
					<th>Email</th>
					<th>
						<div class="flex flex-row p-1 justify-end gap-3">
							<button
								type="button"
								class="btn-icon hover:variant-filled"
								use:popup={printPopupHover}
							>
								<Icon icon="material-symbols:print" />
							</button>
							<button
								type="button"
								class="btn-icon hover:variant-filled"
								use:popup={exportPopupHover}
							>
								<Icon icon="ph:export" />
							</button>
							<button
								type="button"
								class="dots-menu btn-icon hover:variant-filled"
								on:click={toggleDropdown}
							>
								<Icon icon="charm:menu-kebab" width="20" height="20" />
							</button>

							<Dropdown
								triggeredBy=".dots-menu"
								open={isDropdownOpen}
								class="bg-red-600 w-48 h-auto p-2 absolute -right-11 top-2 rounded-md"
							>
								<DropdownItem>Dashboard</DropdownItem>
								<DropdownItem>Settings</DropdownItem>
								<DropdownItem>Earnings</DropdownItem>
							</Dropdown>
						</div>
					</th>
				</tr>
			</thead>

			<tbody>
				<!-- svelte-ignore a11y-mouse-events-have-key-events -->
				<Contactbox/>
				<Contactbox/>
				<Contactbox/>
				<Contactbox/>
			</tbody>

			<!-- <tfoot>
			<tr>
				<th colspan="3">Calculated Total Weight</th>
				<td>totalWeight</td>
			</tr>
		</tfoot> -->
		</table>
	</div>

	<!-- 
    <div class="grid grid-cols-7 row-span-2">
        <div class="bg-blue-400"></div>
		<div class="bg-yellow-400"></div>
		<div class="bg-black-400"></div>
		<div class="bg-red-400"></div>
		<div class="bg-purple-400"></div>
		<div class="bg-pink-400"></div>
		<div class="bg-green-400"></div>
    </div> -->
</div>

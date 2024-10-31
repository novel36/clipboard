<script lang="ts">
	import Icon from '@iconify/svelte';
	import { getDrawerStore, popup, type PopupSettings } from '@skeletonlabs/skeleton';
	import { Button, Dropdown, DropdownItem, ToolbarButton, DropdownDivider } from 'flowbite-svelte';
	let toggle = false;
	let isContactHovered = false;
	let isDropdownOpen = false;
	let isFavorite = false;

	function toggleFavorite() {
		isFavorite = !isFavorite ? true : false;
		console.log('favorite clicked');
	}
	function toggleDropdown() {
		toggle = !isDropdownOpen ? true : false;
	}
	function contactHovered() {
		isContactHovered = true;
		console.log(isContactHovered);
	}
	function contactHoveredLeave() {
		isContactHovered = false;
		console.log(isContactHovered);
	}
	const drawerStore = getDrawerStore();
	function drawerClose() {
		drawerStore.close();
	}

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
				<tr
					on:mouseenter={() => contactHovered()}
					on:mouseleave={() => contactHoveredLeave()}
					class=""
				>
					<td>
						<div class="flex flex-row items-center gap-3">
							{#if !isContactHovered}
								<img
									class="cursor-pointer object-fill w-9 placeholder-circle"
									src="https://images.unsplash.com/photo-1617296538902-887900d9b592?ixid=M3w0Njc5ODF8MHwxfGFsbHx8fHx8fHx8fDE2ODc5NzExMDB8&ixlib=rb-4.0.3&w=128&h=128&auto=format&fit=crop"
									alt=""
								/>
							{:else}
								<input class="checkbox text-3xl w-9 h-9" type="checkbox" />
							{/if}

							Novel Wolde
						</div>
					</td>
					<td class="">
						<div class="h-9 flex items-center">0911223547</div>
					</td>
					<td>
						<div class="h-9 flex items-center">novelwolde@gmail.com</div>
					</td>
					{#if isContactHovered}
						<td>
							<div class="h-9 flex flex-row justify-end gap-3 items-center">
								<button
									type="button"
									class="dots-menu btn-icon hover:variant-filled"
									on:click={() => toggleFavorite()}
								>
									{#if !isFavorite}
										<Icon class="btn-icon hover:variant-filled " icon="uil:favorite" on:click />
									{:else}
										<Icon icon="uim:favorite" />
									{/if}
								</button>
								<button
									type="button"
									class="dots-menu btn-icon hover:variant-filled"
									on:click={toggleDropdown}
								>
									<Icon class="btn-icon hover:variant-filled " icon="ic:outline-edit" /></button
								>

								<!-- <Icon class="btn-icon hover:variant-filled " icon="charm:menu-kebab"/> -->
								<button
									type="button"
									class="data-menu btn-icon hover:variant-filled"
									on:click={toggleDropdown}
								>
									<Icon icon="charm:menu-kebab" />
								</button>
								<Dropdown
									triggeredBy=".data-menu"
									open={isDropdownOpen}
									class="bg-red-600 w-48 h-auto p-2 absolute -right-11 top-2 rounded-md"
								>
									<DropdownItem>Dashboard</DropdownItem>
									<DropdownItem>Settings</DropdownItem>
									<DropdownItem>Earnings</DropdownItem>
								</Dropdown>
							</div>
						</td>
					{/if}
				</tr>
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

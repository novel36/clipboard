<script lang="ts">
	import Icon from '@iconify/svelte';
	import { Avatar } from '@skeletonlabs/skeleton';
	import TelInput from '$lib/inputbox/telInput.svelte';
	import type { E164Number } from 'svelte-tel-input/types';
	let phoneInputValue: E164Number ;


</script>

<div class="flex flex-col pt-6 px-3 gap-1">
	<!-- save -->
	<div
		class="flex justify-between h-16 w-[680px] variant-outline rounded-xl items-center px-3 py-1"
	>
		<!-- back button -->
		<div class="w-16">
			<a href="/addcontact" class="btn-icon variant-outline">
				<Icon icon="bx:arrow-back" />
			</a>
		</div>
		<!-- action -->
		<div class="  flex-1 p-2 flex justify-end gap-3">
			<a href="/addcontact" class="btn-icon variant-outline">
				<Icon icon="fluent-mdl2:favorite-star" />
			</a>
			<button type="button" class="btn variant-outline">save</button>
		</div>
	</div>
	<!-- contact info -->

	<div class=" h-44 p-2">
		<div class="relative inline-block w-40 p-2 h-40">
			<span class="badge-icon absolute bottom-6 right-5 z-10">
				<button class="btn-icon shadow-gray-900">
					<Icon icon="carbon:add-filled" width="42" height="42" class="text-secondary-400 " />
				</button>
			</span>
			<Avatar width="w-36" />
		</div>

		<div class="w-[520px] flex flex-col gap-5 mt-5">
			<div class="input-group input-group-divider grid-cols-[auto_1fr_auto]">
				<div class="input-group-shim">
					<Icon icon="iconamoon:profile-light" />
				</div>
				<input type="text" placeholder="Firstname" />
			</div>
			<div class="input-group input-group-divider grid-cols-[auto_1fr_auto]">
				<div class="input-group-shim">
					<Icon icon="iconamoon:profile-light" />
				</div>
				<input type="text" placeholder="Lastname(optional)" />
			</div>
			<div class="input-group input-group-divider grid-cols-[auto_1fr_auto]">
				<div class="input-group-shim">
					<Icon icon="iconamoon:profile-light" />
				</div>
				<input type="tel" placeholder="Phone" />
			</div>
			<TelInput value={phoneInputValue ?? ''} selectedCountry="ET" valid={false} options={{}} />
		</div>
	</div>
</div>

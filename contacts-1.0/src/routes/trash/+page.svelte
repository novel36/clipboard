<script>
    import { Button, Dropdown, DropdownItem, ToolbarButton, DropdownDivider } from 'flowbite-svelte';
    import { DotsHorizontalOutline, DotsVerticalOutline } from 'flowbite-svelte-icons';
  </script>
  <div class="w-full flex justify-center">
     <DotsVerticalOutline class="dots-menu dark:text-white" />
  <Dropdown triggeredBy=".dots-menu">
    <DropdownItem>Dashboard</DropdownItem>
    <DropdownItem>Settings</DropdownItem>
    <DropdownItem>Earnings</DropdownItem>
    <DropdownItem slot="footer">Sign out</DropdownItem>
  </Dropdown>
  </div>
 
<template>
    <div class="flex flex-col">
    <LayoutHeader>
        <template #left-header>
            <div class="text-lg font-medium text-gray-900">Supplier</div>
        </template>
    </LayoutHeader>
    <ListViewBuilder
        ref="listViewRef"
        :options="options"
        @row-click="openSupplier"
        @empty-state-action="isDialogVisible = true"
    />
    </div>
</template>
<script setup lang="ts">
    import { computed, ref, h } from "vue";
    import { usePageMeta, Avatar } from "frappe-ui";
    import { ListViewBuilder, LayoutHeader } from "@/components";
    import { PhoneIcon } from "@/components/icons";

    const isDialogVisible = ref(false);
    const isSupplierDialogVisible = ref(false);
    const selectedSupplier = ref(null);
    
    const listViewRef = ref(null);
    const options = computed(() => {
    return {
        doctype: "Supplier",
        columnConfig: {
            full_name: {
            prefix: ({ row }) => {
                return h(Avatar, {
                shape: "circle",
                image: row.image,
                label: row.name,
                size: "sm",
                });
            },
            },
            mobile_no: {
            prefix: PhoneIcon,
            },
        },
        emptyState: {
            title: "No Supplier Found",
        },
        };
    });
    
    function openSupplier(id: string): void {
        selectedSupplier.value = id;
        isSupplierDialogVisible.value = true;
    }
    
    usePageMeta(() => {
        return {
        title: "Supplier",
        };
    });
    </script>
<script setup lang="ts">
let ClassicEditor: any;
let CKEditor: { component: { template: string } };

if (process.client) {
    ClassicEditor = require('@ckeditor/ckeditor5-build-classic');
    CKEditor = require('@ckeditor/ckeditor5-vue2');
} else {
    CKEditor = { component: { template: '<div></div>' } };
}

const value = ref<string>('');
const editorConfig = ref<any>({});
</script>
<template>
    <ckeditor :editor="ClassicEditor" :value="value" :config="editorConfig" @input="(event: any) => $emit('input', event)" />
</template>

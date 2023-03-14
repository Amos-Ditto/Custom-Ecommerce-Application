<script setup lang="ts">
import Editor from "@tinymce/tinymce-vue";
const content = ref<string>("");
</script>
<template>
	<div class="w-full flex flex-col mt-4">
		<Editor
			api-key="ast0i3xjqao99fmvcg67egnscyr27xgmve92ah5w465q4uuw"
			:init="{
				plugins: 'lists link image table code help wordcount',
			}"
			v-model="content"
		/>
	</div>
</template>

<script setup lang="ts">
useHead({
    script: [{ src: 'https://cdn.jsdelivr.net/npm/tw-elements/dist/js/index.min.js' }],
})
</script>
<template>
    <div class="w-full h-full flex flex-col">
        <div id="carouselExampleIndicators" class="carousel slide relative w-full h-full" data-bs-ride="carousel">
            <div class="carousel-indicators absolute right-0 bottom-0 left-0 flex justify-center p-0 mb-4">
                <button
                    type="button"
                    data-bs-target="#carouselExampleIndicators"
                    data-bs-slide-to="0"
                    class="active"
                    aria-current="true"
                    aria-label="Slide 1"
                ></button>
                <button type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide-to="1" aria-label="Slide 2"></button>
                <!-- <button type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide-to="2" aria-label="Slide 3"></button> -->
            </div>
            <div class="carousel-inner relative w-full h-full overflow-hidden">
                <div class="carousel-item active float-left w-full h-full">
                    <div class="c-body w-full h-full grid grid-cols-2 bg-[url('assets/images/c-bg.webp')] bg-contain rounded-sm md:px-2">
                        <div class="h-full flex flex-col items-center justify-center gap-y-6 xs:pl-1 md:pl-2 lg:pl-4">
                            <h3
                                class="text-center font-bold text-xl md:text-2xl xl:text-3xl tracking-normal md:tracking-wide text-[#ffea2b]"
                            >
                                Shopping has become <br />
                                more convenient
                            </h3>
                            <button
                                class="text-sm md:text-base tracking-wide bg-[#ff9c19] text-gray-50 px-4 lg:px-8 py-2 rounded-sm hover:bg-opacity-90"
                            >
                                Let's shop
                            </button>
                        </div>
                        <div class="h-full flex items-center justify-center">
                            <img src="~/assets/images/shop_bg.webp" alt="" class="w-full scale-150" />
                        </div>
                    </div>
                </div>
                <div class="carousel-item float-left w-full h-full">
                    <div
                        class="c-body w-full h-full flex flex-col items-center justify-center bg-[url('assets/images/c-bg.webp')] bg-contain rounded-sm px-2 md:px-8"
                    >
                        <div class="img-component w-full h-full flex items-center justify-center">
                            <img src="~/assets/images/c_2.webp" alt="" class="" />
                        </div>
                        <button
                            class="absolute bottom-[14%] md:bottom-[12%] text-sm md:text-base tracking-wide bg-[#ff9c19] text-gray-50 px-8 py-2 rounded-sm hover:bg-opacity-90"
                        >
                            Let's start
                        </button>
                    </div>
                </div>
                <!-- <div class="carousel-item float-left w-full h-full">
                    <div
                        class="c-body w-full h-full flex flex-col items-center justify-center bg-[url('assets/images/c-bg.webp')] bg-contain rounded-sm px-2 md:px-8"
                    ></div>
                </div> -->
            </div>
            <button
                class="carousel-control-prev absolute top-0 bottom-0 flex items-center justify-center p-0 text-center border-0 hover:outline-none hover:no-underline focus:outline-none focus:no-underline -left-5 md:-left-8"
                type="button"
                data-bs-target="#carouselExampleIndicators"
                data-bs-slide="prev"
            >
                <span class="carousel-control-prev-icon inline-block bg-no-repeat" aria-hidden="true"></span>
                <span class="visually-hidden">Previous</span>
            </button>
            <button
                class="carousel-control-next absolute top-0 bottom-0 flex items-center justify-center p-0 text-center border-0 hover:outline-none hover:no-underline focus:outline-none focus:no-underline -right-5 md:-right-8"
                type="button"
                data-bs-target="#carouselExampleIndicators"
                data-bs-slide="next"
            >
                <span class="carousel-control-next-icon inline-block bg-no-repeat" aria-hidden="true"></span>
                <span class="visually-hidden">Next</span>
            </button>
        </div>
    </div>
</template>

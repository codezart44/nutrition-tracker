<script lang="ts">
    // import kohlrabi 
    let text = "";
    $: test(text)
    let fdc_id = 168424;

    type Food = {
        fdc_id: number,
        description: string,
        category: string,
    }

    let results: Food[] = [];

    function test(text: String) {
        if (text.length < 3) return;
        console.log("Query for", text);
    }

    async function searchFoods() {
        // if (text.length < 2) return [];
        const response = await fetch("http://127.0.0.1:5000/foods", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ fdc_ids: [fdc_id] })
        });

        results = await response.json()
    }
</script>

<div>
    <input type="text" bind:value={text}/>
    <button onclick={searchFoods}>search</button>
    {#each results as food}
        <p>{food.description}</p>
    {/each}

    <img src="/food_icons/vegetables/svg/kohlrabi-red.svg" alt="kohlrabi-red">
</div>

<style>

</style>

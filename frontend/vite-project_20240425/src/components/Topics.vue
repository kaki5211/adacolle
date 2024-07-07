




<script setup lang="ts">


import Text_1 from './_Text_1.vue';

</script>
<script lang="ts">
export default {
    components: {
      Text_1,
  },

    data () {
      return {
        text_1: "トピックス3",
        desserts: [
          {
            name: '2023-06-14',
            calories: "コンビニ人間",
          },
          {
            name: '2023-06-14',
            calories: '【まとめ】〇〇賞についてまとめました',
          },
          {
            name: '2023-06-14',
            calories: '【考察】今後の本のあり方について',
          },
          {
            name: '2023-06-14',
            calories: '【個人ブログ】好きな小説家について',
          },

        ],
      }
    },
  }
</script>




<template>
  <v-row no-gutters>
    <Text_1 text_1="トピックス" />

    <v-col cols="10" class="mx-auto">
      <v-table>
        <thead>
          <tr>
            <th class="text-left">
              Date
            </th>
            <th class="text-left">
              title
            </th>
          </tr>
        </thead>
        <tbody>
          <tr
            v-for="item in desserts"
            :key="item.name"
          >
            <td>{{ item.name }}</td>
            <td>{{ item.calories }}</td>
          </tr>
        </tbody>
      </v-table>
    </v-col>
  </v-row>
</template>
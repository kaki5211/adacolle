
<script>
// import { Icon } from '@iconify/vue';
// import { mdiAccount } from '@mdi/js'
// import { aliases, mdi } from '@mdi/js'


export default {
  name: '_GlobalStyles',
  data: () => ({
      mdiAccount
    }),
};


</script>






<style>
/* font-weight-black
Bold text.
      Medium weight text.
      Normal weight text.
      Light weight text.
      Thin weight text.
      Italic text.
*/


:root {
  --my-color: #fc7575;
  --my-color-black: #302b2b;
  --my-color-white: #fff5f9;
  --my-color-gray: #cc6685;
  --my-color-green: #c1112e;
}

:root {
  --my-color: #3245c1;
  --my-color-black: #2b2c30;
  --my-color-white: #fff5f9;
  --my-color-gray: #6668cc;
  --my-color-green: #3d11c1;
}

/* :root {
  --my-color: #455045;
  --my-color-black: #2b302b;
  --my-color-white: #f5f8f5;
  --my-color-gray: #9A9;
  --my-color-green: #1aa179;
} */



/* #f5f8f5!important */
.my-text-color { color: var(--my-color)!important;}
.my-text-color-black { color: var(--my-color-black)!important;}
.my-text-color-white { color: var(--my-color-white)!important;}
.my-text-color-gray { color: var(--my-color-gray)!important;}
.my-text-color-green { color: var(--my-color-green)!important;}

.my-bg-color { background-color: var(--my-color)!important;}
.my-bg-color-black { background-color: var(--my-color-black)!important;}
.my-bg-color-white { background-color: var(--my-color-white)!important;}
.my-bg-color-gray { background-color: var(--my-color-gray)!important;}
.my-bg-color-green { background-color: var(--my-color-green)!important;}

.my-border { border:thin solid var(--my-color)!important;}
.my-border-vue { border: thin solid rgba(0,0,0,.12)!important;}
.my-border-bottom { border-bottom: thin solid var(--my-color)!important;}

.my-border-color { border-color: var(--my-color)!important;}
.my-border-color-black { border-color: var(--my-color-black)!important;}
.my-border-color-white { border-color: var(--my-color-white)!important;}
.my-border-color-gray { border-color: var(--my-color-gray)!important;}
.my-border-2 { border-width: 2px!important;}





/* Extra Small (xs): 0px 〜 599px
Small (sm): 600px 〜 959px
Medium (md): 960px 〜 1263px
Large (lg): 1264px 〜 1903px
Extra Large (xl): 1904px 〜 ∞ */

.my-text-size-15 { font-size: 15px!important;}
.my-text-size-20 { font-size: 20px!important;}
.my-text-size-30 { font-size: 30px!important;}
.my-text-size-35 { font-size: 35px!important;}
.my-text-size-40 { font-size: 40px!important;}
.my-text-size-50 { font-size: 50px!important;}

@media (min-width: 600px) {
  .my-text-sm-size-15 { font-size: 15px!important;}
  .my-text-sm-size-20 { font-size: 20px!important;}
  .my-text-sm-size-30 { font-size: 30px!important;}
  .my-text-sm-size-40 { font-size: 40px!important;}
  .my-text-sm-size-50 { font-size: 50px!important;}
}


@media (min-width: 960px) {
  .my-text-md-size-15 { font-size: 15px!important;}
  .my-text-md-size-20 { font-size: 20px!important;}
  .my-text-md-size-30 { font-size: 30px!important;}
  .my-text-md-size-40 { font-size: 40px!important;}
  .my-text-md-size-50 { font-size: 50px!important;}
}
@media (min-width: 1280px) {
  .my-text-lg-size-15 { font-size: 15px!important;}
  .my-text-lg-size-20 { font-size: 20px!important;}
  .my-text-lg-size-30 { font-size: 30px!important;}
  .my-text-lg-size-40 { font-size: 40px!important;}
  .my-text-lg-size-50 { font-size: 50px!important;}
}
@media (min-width: 1920px) {
  .my-text-xl-size-15 { font-size: 15px!important;}
  .my-text-xl-size-20 { font-size: 20px!important;}
  .my-text-xl-size-30 { font-size: 30px!important;}
  .my-text-xl-size-40 { font-size: 40px!important;}
  .my-text-xl-size-50 { font-size: 50px!important;}
}



.my-w-auto { width: auto!important; }






.my-text-contents {
  letter-spacing: 0.03em;
  line-height: 2.5rem;
}



.my-letter-spacing-normal { letter-spacing: normal; }
.my-letter-spacing-initial { letter-spacing: initial; }



.my-text-contents {
  letter-spacing: 0.035em;
  line-height: 2.75rem;
}


.my-letter-spacing {letter-spacing: 3px;}
.my-width-50 {width: 50%!important;}

.my-text-title {
  font-size: 32px;
  line-height: 28px;
  letter-spacing: 4px;
  font-weight: 900;
  text-transform: none;
  tab-size: 4;
  font-family: 'Concert One', sans-serif!important;
}

.my-text-subtitle {
  font-size: 18px;
  line-height: 28px;
  letter-spacing: 3px;
  font-weight: 900;
  text-transform: none;
  tab-size: 4;
  font-family: 'Concert One', sans-serif!important;
}


.font-weight-medium-bold {
  font-weight: 600;
}

.my-fit-contents {
  height: fit-content!important;
}

body { font-family: 'Sawarabi Gothic', sans-serif; }
.my-font-concert-one { font-family: 'Concert One', sans-serif; }

.my-text-margin-05 {
  margin-top: 0.5em;
  margin-bottom: 0.5em;
  padding-top: 0.5em;
  padding-bottom: 0.5em;
}


.my-underline {
  text-decoration: underline;
}


.custom-link {
  color: var(--my-color-black); /* カスタムのリンク色を設定 */
  text-decoration: none;
  /* 他のスタイルをカスタマイズする場合はここに追加 */
}
.custom-link:visited {
  color: var(--my-color-gray); /* 訪問後のリンク色を設定 */
}


</style>

<!-- 


  
  font-weight-black



Black text.

Bold text.

Medium weight text.
font-weight-medium
Normal weight text.

Light weight text.

Thin weight text.

Italic text. -->


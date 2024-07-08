/**
 * plugins/vuetify.ts
 *
 * Framework documentation: https://vuetifyjs.com`
 */

// @ts-ignore

// Styles
import '@mdi/font/css/materialdesignicons.css'
import 'vuetify/styles'

// Composables
import { createVuetify } from 'vuetify'
import defaults from './defaults'

// My
import { VProgressCircular } from 'vuetify/components'


// https://vuetifyjs.com/en/introduction/why-vuetify/#feature-guides
export default createVuetify({
  defaults,
  loader: {
    type: 'circular',  // または 'linear'
  },
  components: {
    VProgressCircular,
  },

  theme: {
    defaultTheme: 'light',
    themes: {
      light: {
        colors: {
          primary: '#472AB2', // プライマリカラー
          secondary: '#4AEAD8', // セカンダリカラー
          accent: '#82B1FF', // アクセントカラー
          error: '#FF5252', // エラーの色
          info: '#2196F3', // 情報の色
          success: '#4CAF50', // 成功の色
          warning: '#FB8C00', // 警告の色
          background: '#DEDEDE', // 背景色
          surface: '#FFFFFF', // 表面の色（カードなど）
          onPrimary: '#FFFFFF', // プライマリカラー上のテキストやアイコンの色
          onSecondary: '#000000', // セカンダリカラー上のテキストやアイコンの色
          onAccent: '#000000', // アクセントカラー上のテキストやアイコンの色
          onError: '#FFFFFF', // エラーカラー上のテキストやアイコンの色
          onInfo: '#FFFFFF', // 情報カラー上のテキストやアイコンの色
          onSuccess: '#FFFFFF', // 成功カラー上のテキストやアイコンの色
          onWarning: '#FFFFFF', // 警告カラー上のテキストやアイコンの色
          onBackground: '#000000', // 背景色上のテキストやアイコンの色
          onSurface: '#000000', // 表面の色上のテキストやアイコンの色
        }
      },
      dark: {
        dark: true,
        colors: {
            primary: '#472AB2',
            secondary: '#4AEAD8',
            accent: '#FF4081',
            error: '#FF5252',
            info: '#2196F3',
            success: '#4CAF50',
            warning: '#FB8C00',
            background: '#303030', // ダークテーマの背景色
            surface: '#424242', // ダークテーマの表面の色
            onPrimary: '#FFFFFF',
            onSecondary: '#000000',
            onAccent: '#000000',
            onError: '#FFFFFF',
            onInfo: '#FFFFFF',
            onSuccess: '#FFFFFF',
            onWarning: '#FFFFFF',
            onBackground: '#FFFFFF', // ダークテーマの背景色上のテキストやアイコンの色
            onSurface: '#FFFFFF', // ダークテーマの表面の色上のテキストやアイコンの色
        }
      },
      mytheme: {
        dark: true,
        colors: {
          primary: '#472AB2',
          secondary: '#4AEAD8',
          accent: '#FF4081',
          error: '#FF5252',
          info: '#2196F3',
          success: '#4CAF50',
          warning: '#FB8C00',
          background: '#303030', // ダークテーマの背景色
          surface: '#424242', // ダークテーマの表面の色
          onPrimary: '#FFFFFF',
          onSecondary: '#000000',
          onAccent: '#000000',
          onError: '#FFFFFF',
          onInfo: '#FFFFFF',
          onSuccess: '#FFFFFF',
          onWarning: '#FFFFFF',
          onBackground: '#FFFFFF', // ダークテーマの背景色上のテキストやアイコンの色
          onSurface: '#FFFFFF', // ダークテーマの表面の色上のテキストやアイコンの色
        }
      }

    }
  }
})



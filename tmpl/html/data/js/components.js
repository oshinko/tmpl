const Components = {
  header: {
    props: {
      title: {
        type: String,
        default: 'Your App Name'
      }
    },
    template: `
      <header>
        <h1>{{ title }}</h1>
      </header>`
  },
  footer: {
    props: {
      copyright: {
        type: String,
        default: 'Your App Name'
      },
      year: {
        type: Number,
        default: Number.parseInt(moment().format('YYYY'))
      }
    },
    template: `
      <footer>
        <small>Copyright © {{ year }} {{ copyright }} All rights reserved.</small>
      </footer>`
  },
  modal: {
    props: {
      open: Boolean
    },
    template: `
      <transition name="modal">
        <div v-if="open" class="modal" @click.stop="$emit('close')">
          <div class="content" @click.stop>
            <slot></slot>
          </div>
        </div>
      </transition>`
  }
}

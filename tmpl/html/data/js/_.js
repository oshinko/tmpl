const STORAGE =
  [undefined, null, '', 'localhost'].includes(window.location.hostname) ?
    sessionStorage :
    localStorage

function sleep(delay) {
  return new Promise(resolve => setTimeout(resolve, delay))
}

const storage = {
  get(key) {
    return JSON.parse(STORAGE.getItem(key))
  },
  set(key, value) {
    if (value instanceof Map)
      value = [...value.entries()].reduce((acc, [k, v]) => {
        acc[k] = v
        return acc
      }, {})
    return STORAGE.setItem(key, JSON.stringify(value))
  },
  remove(key) {
    return STORAGE.removeItem(key)
  }
}

Page({
  onShareAppMessage() {
    return {
      title: '壹周互阅上报1',
      path: 'page/test1'
    }
  },
  data: {
    focus: false,
    inputValue: '',
    items: [
      { value: '【壹周|粉阅群02 20:45到场】', name: '【壹周|粉阅群02 20:45到场】' },
      { value: '【壹周|粉阅群03 20:45到场】', name: '【壹周|粉阅群03 20:45到场】' }
    ]
  },

  checkboxChange(e) {
    console.log('checkbox发生change事件，携带value值为：', e.detail.value)
    const items = this.data.items
    const values = e.detail.value
    for (let i = 0, lenI = items.length; i < lenI; ++i) {
      items[i].checked = false

      for (let j = 0, lenJ = values.length; j < lenJ; ++j) {
        if (items[i].value === values[j]) {
          items[i].checked = true
          break
        }
      }
    }
    this.setData({
      items
    })
  },

  formSubmit(e) {
    console.log('form发生了submit事件，携带数据为：', e.detail.value)
  },

  formReset(e) {
    console.log('form发生了reset事件，携带数据为：', e.detail.value)
    this.setData({
      chosen: ''
    })
  }
 

 

  
})

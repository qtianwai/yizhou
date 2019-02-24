//获取应用实例
var app = getApp();

Page({
  onShareAppMessage() {
    return {
      title: '壹周互阅上报',
      path: 'pages/index/index'
    }
  },
  data: {
    focus: false,
    inputValue: '',
    regFlag: true,
    items: [
      { value: '【壹周|粉阅群02 20:55到场】', name: '【壹周|粉阅群02 20:55到场】' }
      //{ value: '【壹周|粉阅群03 20:45到场】', name: '【壹周|粉阅群03 20:45到场】' }
    ]
  },

  onLoad: function () {
    this.checkLogin();
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

  checkLogin: function () {
    var that = this;
    wx.request({
      url: app.buildUrl('/pinkRead/checkUpload'),
      header: app.getRequestHeader(),
      method: 'POST',
      data: {},
      success: function (res) {
        if (res.data.code != 200) {
          that.setData({
            regFlag: false
          });
          return;
        }
      }
    })

  },

  isURL: function (domain) {
    var name = /[a-zA-Z0-9][-a-zA-Z0-9]{0,62}(\.[a-zA-Z0-9][-a-zA-Z0-9]{0,62})+\.?/;
    if (!(name.test(domain))) {
      return false;
    }
    else {
      return true;
    }
  },

  formSubmit(e) {
    var that = this;
    var data = e.detail.value;
    console.log('form发生了submit事件，携带数据为：', data)
    var ST_GROUPUSERNAME = e.detail.value.ST_GROUPUSERNAME;
    var ST_GZHNAME = e.detail.value.ST_GZHNAME;
    var ST_GZHURL = e.detail.value.ST_GZHURL;
    var ST_GROUPNAME = e.detail.value.ST_GROUPNAME;
    if (ST_GROUPUSERNAME == "") {
      app.tip({ content: '请填写群聊名称~~' });
      return
    }
    if (ST_GZHNAME == "") {
      app.tip({ content: '请填写公众号名称~~' });
      return
    }
    if (ST_GZHURL == "") {
      app.tip({ content: '请粘贴文章链接~~' });
      return
    }
    if (!(this.isURL(ST_GZHURL))) {
      app.tip({ content: '请粘贴正确的文章链接地址~~' });
      return
    }
    if (ST_GROUPNAME == "") {
      app.tip({ content: '请选择所在群聊名称~~' });
      return
    }
    wx.request({
      url: app.buildUrl("/pinkRead/upload"),
      header: app.getRequestHeader(),
      method: 'POST',
      data: data,
      success: function (res) {
        var resp = res.data;
        if (resp.code != 200) {
          app.alert({ "content": resp.msg });
          return;
        }
        wx.navigateTo({    //保留当前页面，跳转到应用内的某个页面（最多打开5个页面，之后按钮就没有响应的）
          url: "success"
        })
      }
    });
  },

  formReset(e) {
    console.log('form发生了reset事件，携带数据为：', e.detail.value)
    this.setData({
      chosen: ''
    })
  }

  
  
})

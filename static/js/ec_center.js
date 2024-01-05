var ec_center = echarts.init(document.getElementById('china'), "dark");

var mydata = [{'name': '上海', 'value': 318}, {'name': '云南', 'value': 162}]

var ec_center_option = {
    title: {
        text: '上市公司区域分布图',
        subtext: '',
        x: 'left'
    },

    tooltip: {
        trigger: 'item'
    },
    //左侧小导航图标
    visualMap: {
        show: true,
        x: 'left',
        y: 'bottom',
        textStyle: {
            fontSize: 8,
        },
        splitList: [{ start: 1,end: 9 },
            {start: 10, end: 49 },
			{ start: 50, end: 99 },
            {  start: 100, end: 499 },
            { start: 500,end: 1000 }],
        color: ['#eb9c34','#ebe534', '#96eb34', '#34ebd9', '#34c6eb', '#F9DCD1']
    },
    //配置属性
    series: [{
        name: '上市公司数量',
        type: 'map',
        mapType: 'china',
        roam: false, //拖动和缩放
        itemStyle: {
            normal: {
                borderWidth: .5, //区域边框宽度
                borderColor: '#62d3ff', //区域边框颜色
                areaColor: "#b7ffe6", //区域颜色
            },
            emphasis: { //鼠标滑过地图高亮的相关设置
                borderWidth: .5,
                borderColor: '#fff',
                areaColor: "#fff",
            }
        },
        label: {
            normal: {
                show: true, //省份名称
                fontSize: 8,
            },
            emphasis: {
                show: true,
                fontSize: 8,
            }
        },
        data:[] //mydata //数据
    }]
};
ec_center.setOption(ec_center_option)
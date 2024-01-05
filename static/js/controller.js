
function get_company_data() {
    $.ajax({
        url:"/fenbu",
        success: function(data) {
			ec_center_option.series[0].data=data.data
            ec_center_option.series[0].data.push({
      	        name:"南海诸岛",value:0,
      	        itemStyle:{
      		        normal:{ opacity:0},
      	        },
      	        label:{show:false}
            })
            ec_center.setOption(ec_center_option)
		},
		error: function(xhr, type, errorThrown) {

		}
    })
}


get_company_data()

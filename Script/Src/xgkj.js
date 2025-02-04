kj();

function kj(){
	$.ajax({
		url: "https://a6tkapi1.com/gallerynew/h5/index/lastLotteryRecord?lotteryType=1&lotteryPage=1", // 地址
		type: "GET", // 请求方式
		dataType: "json",
		success: function(res) {
			var html = '';
			if (res.code === 10000) {
				var data = res.data;
				console.log(data);

				var title_arr = data['title'].split(' ');
				// console.log(title_arr)
				let sxtime=''
				sxtime = title_arr[3].replace('点',':');
				sxtime=sxtime.replace('分','');
				var next_time=title_arr[1]+' '+sxtime+':00';
				console.log("next_time->",next_time);
				// console.log(next_time);

				html+='<div class="new-KJ-TabBox-box-tit">';
				html+='<div class="new-KJ-TabBox-box-tit-l"><img src="static/imgs/gc.png" style="width:14px;margin-right:4px">香港六合彩 第<font class="kj-font-red"><span id="nowYear1"></span><span id="q">'+pad(data['period'], 3)+'</span></font>期</div>';
				html+='<div class="new-KJ-TabBox-box-tit-m">';
				html+='<div class="kj-lotto-tit2">';
				html+='<span class="next_time" data-time="'+next_time+'"></span>';
				html+='<span class="next_time_html"></span>';
				html+='</div>';
				html+='</div>';
				html+='<div class="new-KJ-TabBox-box-tit-r"><a target="_blank" href="' + util.getOfficialUrl() + '" class="kj-font-red"><img id="logo" style="height:30px;"></img></a></div>';
				html+='</div>'
				html+='<div class="new-KJ-TabBox-box-con">';

				for (var i = 0; i < data['numberList'].length; i++) {
					var color = 'background-color: rgb(153, 153, 153); color: rgb(0, 0, 0);';
					if (data['numberList'][i]['color'] === 1) {
						color = 'background-color: rgb(231, 22, 7); color: rgb(255, 255, 255);';
					} else if (data['numberList'][i]['color'] === 2) {
						color = 'background-color: rgb(35, 137, 233); color: rgb(255, 255, 255);';
					} else if (data['numberList'][i]['color'] === 3) {
						color = 'background-color: rgb(31, 182, 29); color: rgb(255, 255, 255);';
					}

					var shengXiao = '';
					if (data['numberList'][i]['shengXiao'] !== undefined) {
						shengXiao = data['numberList'][i]['shengXiao'];
					}
					var wuXing = '';
					if (data['numberList'][i]['wuXing'] !== undefined) {
						wuXing = data['numberList'][i]['wuXing'];
					}

					if(data['numberList'][i]['color']){
						var windex='w'+data['numberList'][i]['color'];
						var sindex='m'+data['numberList'][i]['color'];
					}else{
						var windex='w9';
						var sindex='m9';
					}

					html+='<div id="'+windex+'" class="kj-ball box m0">';
					html+=' <h2> <div id="'+sindex+'">'+data['numberList'][i]['number']+'</div> </h2>';
					html+='<div id="'+sindex+'x" class="whsx">'+wuXing+'/'+shengXiao+'</div>';
					html+='</div>';
				}
				html+='</div>';

				var next_qi = parseInt(title_arr[0].substring(1));
				var next_day_arr = title_arr[1].split('/');
				var next_time_arr = title_arr[2].split(':');
				var next_qi_week = title_arr[3];

				html+='<div class="new-KJ-TabBox-box-foot">';
				html+='<div class="new-KJ-TabBox-box-foot-l">第<font class="kj-font-red"><span id="nowYear2"></span><span id="nextQiShu">'+data['nextLotteryNumber']+'</span></font>期：<span id="nextMonth">'+next_day_arr[1]+'</span>月<span id="nextDay">'+next_day_arr[2]+'</span>日 <span id="nextWeek">'+next_time_arr[0]+'</span> <span id="nextTime">'+next_qi_week+'</span></div>';
				html+='<div class="new-KJ-TabBox-box-foot-r"><a target="_blank" href="./history/kj.html?type=1" class="kj-font-red">历史记录</a></div> '
				// html+='<div class="new-KJ-TabBox-box-foot-r"><a class="new-KJ-TabBox-box-foot-r-sx" style="cursor:pointer;" onclick="javascript:window.location.reload();">刷新</a></div>';
				html+='</div>';
			}

			$('.new-KJ-TabBox-box').html(html);
			reduct_time(next_time)
			// util.setImage('#logo', '/mess/imgs/gfkj.gif')
		},
		//诊断错误类型
		error: function(jqXHR, textStatus, errorThrown) {
			console.log(jqXHR);
			console.log(textStatus);
			console.log(errorThrown);
		}
	});
}
let clearFirstTime = null // 定时器
let fristEndTime = '2023/05/09 21:30:00'//结束时间

function reduct_time(next_time){
	let curDay = new Date()// 当前时间
	let hour = '00'
	let minute = '00'
	let second = '00'

	// let fristEndTime = '2023/05/09 21:30:00'//结束时间
	fristEndTime = next_time
	// console.log(fristEndTime);
	clearFirstTime = setInterval(setStarTime, 1000)
}

function setStarTime() {
	let that = this
	let date = new Date()
	let now = date.getTime()
	let endDate = new Date(fristEndTime)
	let end = endDate.getTime()
	let leftTime = end - now
	let d = null
	let h = null
	let m = null
	let s = null
	// console.log(leftTime)
	if (leftTime >= 0) {
		d = Math.floor(leftTime / 1000 / 60 / 60 / 24)
		h = Math.floor(leftTime / 1000 / 60 / 60 % 24)
		h = d * 24 + h
		m = Math.floor(leftTime / 1000 / 60 % 60)
		s = Math.floor(leftTime / 1000 % 60)
		hour = h < 10 ? '0' + h : h
		minute = m < 10 ? '0' + m : m
		second = s < 10 ? '0' + s : s
	} else {
		// reducedTime()
		hour = '00'
		minute = '00'
		second = '00'
	}

	var html1='<strong id="hour_show"> <s id="h"></s>'+hour+'</strong>:<strong id="minute_show"><s></s>'+minute+'</strong>:<strong id="second_show"><s></s>'+second+'</strong>';
	// console.log(hour, minute, second)
	$('.next_time_html').html(html1)
}



var a, b;

function time() {
	var date = new Date();
	year = date.getFullYear();
	month = date.getMonth() + 1;
	day = date.getDate();
	hours = date.getHours();
	minutes = date.getMinutes();
	seconds = date.getSeconds();

	if (hours != 21) {
		return;
	}

	if (hours == 21 && (minutes >= 29 && minutes <= 40)) {
		kj();
	}

	if (hours == 21 && minutes > 40) {
		// kj();
		clearInterval(a);
	}
};

a = setInterval(time, 5000);

function pad(num, n) {
	var len = num.toString().length;
	while (len < n) {
		num = "0" + num;
		len++;
	}
	return num;
}

util.onHeightChange(document.querySelector('.new-KJ-TabBox-box'), 'xgkj')

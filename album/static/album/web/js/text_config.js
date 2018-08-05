// 配置
var textCfg = [
  function() { // 1.png
    return {
      elem: '<div style="width: 190px; height: 130px; position: absolute; display: table; text-align: center; background: url('+staticUrl+'/img/text/1.png) center center no-repeat; background-size: 100% 100%; overflow: hidden; "> <div class="textValue" style="display: table-cell; vertical-align: middle; padding: 1px 55px 0px 55px;color: #DD6D64;font-size: 12px;"> </div> </div>',
      animate: {
        animate : {'name':'animate1','duration':15},
        beginCss : {'top':'10%','bottom':undefined,'left':'-100%','right':undefined},
        endCss : {'top':'10%','left':'5%'}
      },
    }
  },
  function () { // 2.png
    return {
      elem: '<div style="width: 150px; height: 140px; position: absolute; display: table; text-align: center; background: url('+staticUrl+'/img/text/2.png) center center no-repeat; background-size: 100% 100%; overflow: hidden; "> <div class="textValue" style="display: table-cell; vertical-align: middle; padding: 20px 20px 20px 40px;font-size: 12px;"> </div> </div>',
      animate: {
        animate : {'name':'animate1','duration':10},
        beginCss : {'top':'35%','bottom':undefined,'left':undefined,'right':'-100%'},
        endCss : {'top':'35%','right':'10%'}
      },
    }
  },
  function () { // 3.png
    return {
      elem: '<div style="width: 180px; height: 116px; position: absolute; display: table; text-align: center; background: url('+staticUrl+'/img/text/3.png) center center no-repeat; background-size: 100% 100%; overflow: hidden;"> <div class="textValue" style="display: table-cell; vertical-align: middle; padding: 10% 20% 10% 40%;color: #F9E5C8;font-size: 12px;"></div> </div>',
      animate: {
        animate : {'name':'animate2','duration':15},
        beginCss : {'top':undefined,'bottom':'25%','left':'-100%','right':undefined},
        endCss : {'bottom':'25%','left':'20px'}
      },
    }
  },
  function () { // 5.png
    return {
      elem: '<div style="width: 180px; height: 130px; position: absolute; display: table; text-align: center; background: url('+staticUrl+'/img/text/5.png) center center no-repeat; background-size: 180px 130px; overflow: hidden; "> <div class="textValue" style="display: table-cell; vertical-align: middle; padding: 0% 20% 3% 20%;font-size: 12px;"></div> </div>',
      animate: {
        animate : {'name':'animate3','duration':15},
        beginCss : {'top':undefined,'bottom':'25%','left':'-100%','right':undefined},
        endCss : {'bottom':'25%','left':'20px'}
      },
    }
  },
  function () { // 6.png
    return {
      elem: '<div style="width: 180px; height: 110px; position: absolute; display: table; text-align: center; background: url('+staticUrl+'/img/text/6.png) center center no-repeat; background-size:  180px 110px; overflow: hidden; "> <div class="textValue" style="display: table-cell; vertical-align: middle; padding: 8% 20% 13% 20%;color: #9A5B3A;font-size: 12px;"> </div> </div>',
      animate: {
        animate : {'name':'animate3','duration':15},
        beginCss : {'top':'35%','bottom':undefined,'left':undefined,'right':'-100%'},
        endCss : {'top':'35%','right':'10%'}
      },
    }
  },
  function () { // 8.png
    return {
      elem: '<div style="width: 140px; height: 180px; position: absolute; display: table; text-align: center; background: url('+staticUrl+'/img/text/8.png) center center no-repeat; background-size: 100% 100%; overflow: hidden;"> <div class="textValue" style="display: table-cell; vertical-align: middle; padding: 6% 12% 56% 28%;font-size: 12px;color: #fff;"></div> </div>',
      animate: {
        animate : {'name':'animate4','duration':20},
        beginCss : {'top':'50%','bottom':undefined,'left':'-100%','right':undefined},
        endCss : {'top':'50%','left':'20px'}
      },
    }
  },
  function () { // 7.png
    return {
      elem: '<div style="width: 140px; height: 180px; position: absolute; display: table; text-align: center; background: url('+staticUrl+'/img/text/7.png) center center no-repeat; background-size: 100% 100%; overflow: hidden;"> <div class="textValue" style="display: table-cell; vertical-align: middle; padding: 0% 10% 42% 10%;color: #fff;font-size: 12px;"></div> </div>',
      animate: {
        animate : {'name':'animate5','duration':20},
        beginCss : {'top':'50%','bottom':undefined,'left':undefined,'right':'-100%'},
        endCss : {'top':'50%','right':'5%'}
      },
    }
  },
  function () { // 9.png
    return {
      elem: '<div style="width: 130px; height: 130px; position: absolute; display: table; text-align: center; background: url('+staticUrl+'/img/text/9.png) center center no-repeat; background-size: 100% 100%; overflow: hidden;"><div class="textValue" style="display: table-cell; vertical-align: middle; padding: 0% 20% 0% 20%;color: #7399BF;font-size: 12px;"></div></div>',
      animate: {
        animate : {'name':'animate6','duration':10},
        beginCss : {'top':'20%','bottom':undefined,'left':'-100%','right':undefined},
        endCss : {'top':'20%','left':'20px'}
      },
    }
  },
];
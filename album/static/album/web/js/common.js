function escapeHtml(text) {
    if (text.length == 0) { return "" };

    var map = {
        '&': '&amp;',
        '<': '&lt;',
        '>': '&gt;',
        '"': '&quot;',
        "'": '&#039;',
        " ": '&nbsp;'
    };

    return text.replace(/[&<>"' ]/g, function (m) { return map[m]; });
}

function decodeEscapeHtml(text) {
    if (text.length == 0) { return "" };

    var map = {
        '&amp;': '&',
        '&lt;': '<',
        '&gt;': '>',
        '&quot;': '"',
        '&#039;': "'",
        '&nbsp;': ' '
    };

    return text.replace(/(&nbsp;|&amp;|&lt;|&gt;|&quot;|&#039;)/g, function (m) { return map[m]; });
}

/* textPlayer **********************************/
var textPlayer = {
    // 文本节点创建器
    textNodeCreater: function (elem, endCallBack, endCallBackThis) {
        this._node = $(elem.elem);
        this._animate = elem.animate;

        // 设置动画回调
        if (endCallBack) {
            this._node.bind('oanimationend animationend webkitAnimationEnd',
              function () {
                  endCallBack.call(endCallBackThis);
              }
            );
        }

        // 动画设置
        /* var _this = this;
        this._node.bind('oanimationstart animationstart webkitAnimationStart',
            function() {
              if(_this.animateCss) {
                _this.css(_this.animateCss);
              }
            }
        ); */

        // 设置文接口
        this.setTextValue = function (val) {
            this._node.find('.textValue').html(val);
        };

        // 设置动画接口
        this.setAnimate = function (cfg) {
            // 播放时间
            var time = cfg.duration + 's';
            // 延迟时间
            var delayTime = '0s';
            if (cfg.delay) {
                delayTime = cfg.delay + 's';
            }
            // 播放函数
            var timeFunc = cfg.timeFunc;
            if (!timeFunc) {
                timeFunc = 'ease';
            }

            var animate = [cfg.name, time, timeFunc, delayTime].join(' ');
            this.css({
                '-webkit-animation': animate,
                'animation': animate,
            });
        }

        // 设置 css 接口.
        this.css = function (val) {
            this._node.css(val);
        }
    },
    /***********/

    // 显示元素
    _displayDiv: undefined,
    _textNodes: [], // 文本节点

    // 配置文件
    _textCfgs: undefined,
    _animateCfgs: undefined,

    // 文本索引
    _textIdx: 0,
    _textNodeIdx: 0,
    _playCount: 0,
    _playRoundEnd: 0,
    _roundSleepTime: 5000,
    _intervalSleepTime: 2000,

    start: function (textArr, textConfig) {
        if (textArr.length <= 0) {
            console.log('no text!');
            return;
        };

        this._textCfgs = textConfig;

        var random = Math.random();
        // 生成乱序效果
        for (var i = 0, len = Math.floor(this._textCfgs.length / 2) ; i < len; ++i) {
            var oPos = Math.floor(random * (i + 1) * 173) % this._textCfgs.length;
            var nPos = Math.floor(random * (i + 1) * 34) % this._textCfgs.length;
            var tmp = this._textCfgs[oPos];
            this._textCfgs[oPos] = this._textCfgs[nPos];
            this._textCfgs[nPos] = tmp;
        }

        this._textArr = [];

        for (var i = 0, len = textArr.length; i < len; ++i) {
            var text = textArr[i];
            if (text.length > 0) {
				console.log();
                this._textArr.push(decodeURI(escapeHtml(textArr[i])));
            }
        }

        this._displayDiv = $('.TextView');
        this.playNext();
    },

    playNext: function () {
        this._displayDiv[0].innerHTML = "";

        var textNode = undefined;
        var nodeIdx = this._textNodes.length;
        var random = Math.random();

        for (var i = 0, len = 1; i < len; ++i) {
            // 获取配置
            if (nodeIdx + i < this._textCfgs.length || this._textNodes.length <= 0) {
                var cfgIdx = nodeIdx + i;
                // 若需显示个数大于文字效果个数随机生成几个.
                if (cfgIdx > this._textCfgs.length - 1) {
                    cfgIdx = Math.floor(random * this._textCfgs.length);
                }
                textNode = new this.textNodeCreater(this._textCfgs[cfgIdx](), this.playEnd, this);
                this._textNodes.push(textNode);
            } else {
                textNode = this._textNodes[this._textNodeIdx];
                this._textNodeIdx = (this._textNodeIdx + 1) % this._textNodes.length;
            }
            var animateCfg = textNode._animate;

            textNode.animateCss = animateCfg.endCss;

            // 设置文本信息
            textNode.setTextValue(this._textArr[this._textIdx]);
            textNode.setAnimate(animateCfg.animate);

            // 设置样式
            /* if(animateCfg.beginCss) {
              textNode.css(animateCfg.beginCss);
            } else */ if (animateCfg.endCss) {
          textNode.css(animateCfg.endCss);
      }

            this._textIdx = (this._textIdx + 1) % this._textArr.length;

            if (this._textIdx == 0) {
                this._playRoundEnd = 1;
            }

            this._displayDiv.append(textNode._node);
        }
    },

    playEnd: function () {
        if (--this._playCount <= 0) {
            if (this._playRoundEnd == 1) {
                this._playRoundEnd = 0;
                this._displayDiv[0].innerHTML = "";

                // 回合直接的间隔
                setTimeout(function () {
                    textPlayer.playNext();
                }, this._roundSleepTime);
            } else {
                this._displayDiv[0].innerHTML = "";

                setTimeout(function () {
                    textPlayer.playNext();
                }, this._intervalSleepTime);

            }
        }
    }
}
!function(e){var o={title:"",message:"",type:"success",duration:5e3},n=function(t){t.removeClass("show"),setTimeout(function(){t.remove(),e(".custom-toast-container .custom-toast").length === 0&&e("#customToastContainer").remove()},300)};e.toast=function(t){var s=e.extend({},o,t);return e("#customToastContainer").length === 0&&(t=e("<div>").addClass("custom-toast-container").attr("id","customToastContainer"),e("body").append(t)),function(t){switch(t.type){case"success":default:svgIcon='<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512"><path d="M256 512A256 256 0 1 0 256 0a256 256 0 1 0 0 512zM241 337l-17 17-17-17-80-80L161 223l63 63L351 159 385 193 241 337z"></path></svg>';break;case"error":svgIcon='<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512"><path d="M256 512A256 256 0 1 0 256 0a256 256 0 1 0 0 512zm97.9-320l-17 17-47 47 47 47 17 17L320 353.9l-17-17-47-47-47 47-17 17L158.1 320l17-17 47-47-47-47-17-17L192 158.1l17 17 47 47 47-47 17-17L353.9 192z"/></svg>';break;case"info":svgIcon='<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512"><path d="M256 512A256 256 0 1 0 256 0a256 256 0 1 0 0 512zM216 336h24V272H216 192V224h24 48 24v24 88h8 24v48H296 216 192V336h24zm72-144H224V128h64v64z"/></svg>';break;case"warning":svgIcon='<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512"><path d="M256 512A256 256 0 1 0 256 0a256 256 0 1 0 0 512zm24-384v24V264v24H232V264 152 128h48zM232 368V320h48v48H232z"/></svg>'}var s='<div class="custom-toast '+t.type+'"><div class="icon-container">'+svgIcon+'</div><div class="content-container"><p class="title">'+t.title+'</p><p class="message">'+t.message+'</p></div><button class="close-button">&times;</button></div>',o=e(s).appendTo("#customToastContainer");return setTimeout(function(){n(o)},t.duration),o.find(".close-button").click(function(){n(o)}),setTimeout(function(){o.addClass("show")},100),o}(s)}}(jQuery);

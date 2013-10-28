<!DOCTYPE html>
<html>
  <head>
    <title>FontView</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link id="bootstrap_style" href="//netdna.bootstrapcdn.com/bootswatch/3.0.0/{{ theme }}/bootstrap.min.css" rel="stylesheet">
    <link id="source_style" href="/style/{{ style }}" rel="stylesheet">
    <link href="//netdna.bootstrapcdn.com/font-awesome/3.2.1/css/font-awesome.min.css" rel="stylesheet">
    <link href="/static/css/style.css" rel="stylesheet">

    <!--[if lt IE 9]>
      <script src="//cdnjs.cloudflare.com/ajax/libs/html5shiv/r29/html5.min.js"></script>
      <script src="//cdnjs.cloudflare.com/ajax/libs/respond.js/1.2.0/respond.min.js"></script>
    <![endif]-->
  </head>
  
  <body>
      <div class="row">
        <div class="col-sm-11">
          {{! code }}
        </div>
        
        <div class="col-sm-1" data-spy="affix">
            <ins class="adsbygoogle"
                style="display:inline-block;width:160px;height:600px"
                data-ad-client="ca-pub-7855868022998589"
                data-ad-slot="3376498158"></ins>
            
        </div>
      </div>
        
        <div id="footer" class="navbar navbar-default navbar-fixed-bottom">
            <form class="form-inline">
              <label for="font_select">font
                <select id="font_select" class="form-control input-sm">
              %key = lambda x: '' if x == 'monospace' else x
              %for item in sorted(fonts, key=key):
                  %title = item if item != 'monospace' else 'Browser Default'
                  %name = item.lower().replace(' ', '')
                  %selected = ' selected' if name == font else ''
                  <option value="{{ item }}"{{ selected }}>
                    {{ title }}
                  </option>
              %end
                </select>
              </label>
              
              <label for="size_select">size
                <select id="size_select" class="form-control input-sm">
              %for item in range(1, 65):
                  %selected = ' selected' if str(item) == size else ''
                  <option value="{{ item }}"{{ selected }}>
                    {{ item }} pt
                  </option>
              %end
                </select>
              </label>
                    
              <label for="style_select">style
                <select id="style_select" class="form-control input-sm">
              %for item in sorted(styles):
                %if item == style:
                  <option selected>
                %else:
                  <option>
                %end
                    {{ item.title() }}
                  </option>
              %end
                </select>
                </label>
                
              <label for="theme_select">theme
                <select id="theme_select" class="form-control input-sm">
              %for item in sorted(themes):
                %if item == theme:
                  <option selected>
                %else:
                  <option>
                %end
                    {{ item.title() }}
                  </option>
              %end
                </select>
              </label>
        
              <a id="permalink">permalink</a>
              <span class="links pull-right">
                <a target="_blank" href="https://github.com/dhagrow/fontview">
                  <i class="icon-github-sign"></i>
                </a>
                <a target="_blank" href="https://twitter.com/intent/tweet?url=http://fonts.dhagrow.org/&text=Preview Programming Fonts &amp; styles">
                  <i class="icon-twitter-sign"></i>
                </a>
                <a target="_blank" href="https://plus.google.com/share?url=http://fonts.dhagrow.org/">
                  <i class="icon-google-plus-sign"></i>
                </a>
              </span>
            </form>
        </div>

    <script src="//cdnjs.cloudflare.com/ajax/libs/jquery/2.0.3/jquery.min.js"></script>
    <script src="//cdnjs.cloudflare.com/ajax/libs/twitter-bootstrap/3.0.0/js/bootstrap.min.js"></script>
    <script src="//cdnjs.cloudflare.com/ajax/libs/webfont/1.3.0/webfont.js"></script>
    <script src="/static/js/script.js"></script>
    
    <script async src="//pagead2.googlesyndication.com/pagead/js/adsbygoogle.js"></script>
    <script>
        (adsbygoogle = window.adsbygoogle || []).push({});
    </script>
    
  </body>
</html>

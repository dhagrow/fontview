<!DOCTYPE html>
<html>
  <head>
    <title>FontView</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link id="bootstrap_style" href="//netdna.bootstrapcdn.com/bootswatch/3.0.0/{{ theme }}/bootstrap.min.css" rel="stylesheet">
    <link id="source_style" href="/style/{{ style }}" rel="stylesheet">
    <link href="/static/css/style.css" rel="stylesheet">

    <!--[if lt IE 9]>
      <script src="//cdnjs.cloudflare.com/ajax/libs/html5shiv/r29/html5.min.js"></script>
      <script src="//cdnjs.cloudflare.com/ajax/libs/respond.js/1.2.0/respond.min.js"></script>
    <![endif]-->
  </head>
  
  <body>
    <div class="container">
      <div class="row">
        <div class="col-md-10">
          <div class="well">
            {{! code }}
          </div>
        </div>
        
        <div class="col-md-2" data-spy="affix">
            <div class="page-header">
              <h2>FontView</h2>
              <div class="subtitle">
                <a href="https://github.com/dhagrow/fontview">source</a>
                <div class="g-plusone" data-size="small" data-annotation="none"></div>
              </div>
            </div>
            
            <form class="form" role="form">
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
              %for item in range(6, 21):
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
            </form>
            
            <a id="permalink">permalink</a>
            
            <hr />
            <ins class="adsbygoogle"
                style="display:inline-block;width:160px;height:600px"
                data-ad-client="ca-pub-7855868022998589"
                data-ad-slot="3376498158"></ins>
            
        </div> <!-- col -->
      </div> <!-- row -->
    </div> <!-- container -->

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

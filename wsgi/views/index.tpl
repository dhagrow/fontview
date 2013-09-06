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
        
        <div class="col-md-2">
            <div class="page-header">
              <h1>FontView</h1>
            </div>
            
            <form class="form" role="form">
              <label for="font_select">font
                <select id="font_select" class="form-control input-sm">
                %key = lambda x: '' if x == 'monospace' else x
              %for item in sorted(fonts, key=key):
                  %title = item.title() if item != 'monospace' else 'Browser Default'
                  %name = item.lower().replace(' ', '')
                  %selected = ' selected' if name == font else ''
                  <option {{ selected }} value="{{ item.title() }}">
                    {{ title }}
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
            
            <hr />
            <a id="permalink">permalink</a>
            
        </div> <!-- col -->
      </div> <!-- row -->
    </div> <!-- container -->

    <script src="//cdnjs.cloudflare.com/ajax/libs/jquery/2.0.3/jquery.min.js"></script>
    <script src="//cdnjs.cloudflare.com/ajax/libs/webfont/1.3.0/webfont.js"></script>
    <script src="/static/js/script.js"></script>
  </body>
</html>

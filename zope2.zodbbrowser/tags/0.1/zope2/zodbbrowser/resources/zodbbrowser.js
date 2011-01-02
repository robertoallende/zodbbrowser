// bottom panel 
var emptyBottom = function(){
    $("#bottom").text("");
    };

var bottom = function(nodepath, panelpath, nodename, kindof) {
    $.ajax({
          url: nodepath + kindof + nodename,
          success: function(data) {
            $('#bottom').html(data);
           }
     });
};

// right panel 
var emptyRight = function(){
    $("#right").text("");
    };

var right = function(nodepath, kind){
    $("#right").dynatree({
          initAjax: {
              url: nodepath + kind,
              data: { mode: "funnyMode" },
              dataType: "json"
              },
      onActivate: function(node) {
        elem = node.data.title;
        switch (kind) {
            case "/class_ancestors" : bottom(nodepath, getPath(node), node.data.title, "/class_source?"); break;
            case "/properties" : bottom(nodepath, getPath(node), node.data.title, "/property_source?"); break;
            case "/callables" : bottom(nodepath, getPath(node), node.data.title, "/method_source?"); break;
            case "/interfaces" : bottom(nodepath, getPath(node), node.data.title, "/interface_source?"); break;
        }
      }
    });
  };

// midle panel 
var emptyMiddle = function(){
    $("#middle").text("");
    };

var middle = function(path){
    $("#middle").dynatree({
              children: [
                        {
                            "title": "Class and Ancestors"
                        }, 
                        {
                            "title": "Properties"
                        }, 
                        {
                            "title": "Callables"
                        }, 
                        {
                            "title": "Interfaces Provided"
                        }
                    ] ,
      onActivate: function(node) {
        switch (node.data.title) {
            case "Properties" : right(path, '/properties') ;  break;
            case "Callables" : right(path, '/callables') ; break;
            case "Interfaces Provided" : right(path, '/interfaces') ; break;
            case "Adapts" : right(path, '/adapts') ; break;
            case "Class and Ancestors" : right(path, '/class_ancestors') ; break;
        }
        // XXX this forces a request twice sometimes
        var rightTree = $("#right").dynatree("getTree");
        rightTree.reload();
      },
      onDeactivate: function(node) {
        emptyRight();
        emptyBottom();
      }
    });
  };


// Just for the left: getPath builds the path traversing the tree
var buildTree = function(node) {
    if (node.data.title) { return ( buildTree(node.parent) + "/" + node.data.title) ; }
    else { return "" ; }
};

var getPath = function(node) {
    var mypath = buildTree(node);
    return mypath.slice(12);
};


// left panel
  $(function(){
    $("#left").dynatree({
          initAjax: {
              url: "/tree",
              data: { mode: "funnyMode" },
              dataType: "json"
              },
      onActivate: function(node) {
        var mypath = getPath(node);
        middle(mypath);
        // XXX this forces a request twice sometimes
        var rightTree = $("#middle").dynatree("getTree");
        rightTree.reload();
      },
      onDeactivate: function(node) {
        emptyRight();
        emptyMiddle();
        emptyBottom();
      },
      onLazyRead: function(node){
                node.appendAjax({
                url: function() { return getPath(node) + "/tree"; }(),
                data: {key: node.data.key,
                       mode: "funnyMode"
                       }
              });
      }
    });
  });



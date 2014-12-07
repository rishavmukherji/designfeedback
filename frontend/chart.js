

var names = {'Aesthetic and Minimalist Design' : 'Aesthetic',
'Consistency and Standard' : 'Consistency',
'Error Prevention' : 'Error Prevention',
'Help Users Recognize, Diagnose, and Recover from Errors' : 'Error Recovery',
'Help and Documentation' : 'Documentation',
'Match between System and the Real World' : 'Match to Real World',
'Recognition rather than recall' : 'Recognition',
'User control and Freedom' : 'User Control',
'Visibility of System Status' : 'Visibility' }

var xformat = function (x) {return names[x];};
var yformat =  function (y) {return parseFloat(y) <= 5 ? y : ''; };
//var data = {'yMin' : 0, 'yMax' : 5.1, 'xScale': 'ordinal', 'comp': [{'className': '.comp.errorBar', 'data': [{'y': 2.7333333333333334, 'x': 'Error Prevention', 'e': 0.23028681044713206}, {'y': 2.9750000000000001, 'x': 'Visibility of System Status', 'e': 0.28529674160289803}, {'y': 2.7749999999999999, 'x': 'Consistency and Standard', 'e': 0.26671674209321861}, {'y': 2.5249999999999999, 'x': 'User Control and Freedom', 'e': 0.27029779399006837}, {'y': 2.7250000000000001, 'x': 'Match between System and the Real World', 'e': 0.20202691260750763}, {'y': 3.9750000000000001, 'x': 'Help and Documentation', 'e': 0.24932601456418765}, {'y': 2.4666666666666668, 'x': 'Recognition rather than recall', 'e': 0.23345436731743885}, {'y': 2.7999999999999998, 'x': 'Aesthetic and Minimalist Design', 'e': 0.27080128015453198}, {'y': 1.7, 'x': 'Help Users Recognize, Diagnose, and Recover from Errors', 'e': 0.27241609041279008}], 'type': 'error'}], 'main': [{'className': '.errorExample', 'data': [{'y': 2.7333333333333334, 'x': 'Error Prevention', 'e': 0.23028681044713206}, {'y': 2.9750000000000001, 'x': 'Visibility of System Status', 'e': 0.28529674160289803}, {'y': 2.7749999999999999, 'x': 'Consistency and Standard', 'e': 0.26671674209321861}, {'y': 2.5249999999999999, 'x': 'User Control and Freedom', 'e': 0.27029779399006837}, {'y': 2.7250000000000001, 'x': 'Match between System and the Real World', 'e': 0.20202691260750763}, {'y': 3.9750000000000001, 'x': 'Help and Documentation', 'e': 0.24932601456418765}, {'y': 2.4666666666666668, 'x': 'Recognition rather than recall', 'e': 0.23345436731743885}, {'y': 2.7999999999999998, 'x': 'Aesthetic and Minimalist Design', 'e': 0.27080128015453198}, {'y': 1.7, 'x': 'Help Users Recognize, Diagnose, and Recover from Errors', 'e': 0.27241609041279008}]}], 'yScale': 'linear'};
var andrew1 = {'yMin' : 0, 'yMax' : 5.1, "yScale": "linear", "xScale": "ordinal","comp": [{"className": ".comp.errorBar", "data": [{"y": 3.4482758620689653, "x": "Error Prevention", "e": 0.22159900371420568}, {"y": 3.7749999999999999, "x": "Visibility of System Status", "e": 0.2569233648086825}, {"y": 3.8157894736842106, "x": "Consistency and Standard", "e": 0.22266733972247066}, {"y": 4.0256410256410255, "x": "User control and Freedom", "e": 0.2219019110943859}, {"y": 4.4210526315789478, "x": "Match between System and the Real World", "e": 0.11434505780210759}, {"y": 4.1842105263157894, "x": "Help and Documentation", "e": 0.21286925296769674}, {"y": 4.2105263157894735, "x": "Recognition rather than recall", "e": 0.1765316824341939}, {"y": 3.75, "x": "Aesthetic and Minimalist Design", "e": 0.24481809049965533}, {"y": 4.2999999999999998, "x": "Help Users Recognize, Diagnose, and Recover from Errors", "e": 0.27241609041279025}], "type": "error"}], "main": [{"className": ".errorExample", "data": [{"y": 3.4482758620689653, "x": "Error Prevention", "e": 0.22159900371420568}, {"y": 3.7749999999999999, "x": "Visibility of System Status", "e": 0.2569233648086825}, {"y": 3.8157894736842106, "x": "Consistency and Standard", "e": 0.22266733972247066}, {"y": 4.0256410256410255, "x": "User control and Freedom", "e": 0.2219019110943859}, {"y": 4.4210526315789478, "x": "Match between System and the Real World", "e": 0.11434505780210759}, {"y": 4.1842105263157894, "x": "Help and Documentation", "e": 0.21286925296769674}, {"y": 4.2105263157894735, "x": "Recognition rather than recall", "e": 0.1765316824341939}, {"y": 3.75, "x": "Aesthetic and Minimalist Design", "e": 0.24481809049965533}, {"y": 4.2999999999999998, "x": "Help Users Recognize, Diagnose, and Recover from Errors", "e": 0.27241609041279025}]}]} 
var conference1 = {'yMin' : 0, 'yMax' : 5.1, "yScale": "linear", "xScale": "ordinal", "comp": [{"className": ".comp.errorBar", "data": [{"y": 3.5825461088618984, "x": "Error Prevention", "e": 0.96452918311457403}, {"y": 4.0048920377867745, "x": "Visibility of System Status", "e": 0.21532335314612888}, {"y": 3.9349217638691321, "x": "Consistency and Standard", "e": 0.1521595464450598}, {"y": 4.2323968705547657, "x": "User control and Freedom", "e": 0.18086099376755968}, {"y": 4.4410512486170379, "x": "Match between System and the Real World", "e": 0.11736281777369589}, {"y": 4.2003668648405492, "x": "Help and Documentation", "e": 0.10354521141235926}, {"y": 4.2956215324636382, "x": "Recognition rather than recall", "e": 0.25890623246164085}, {"y": 3.9331983805668016, "x": "Aesthetic and Minimalist Design", "e": 0.15282916699961918}, {"y": 4.2847503373819169, "x": "Help Users Recognize, Diagnose, and Recover from Errors", "e": 0.074224021592443012}], "type": "error"}], "main": [{"className": ".errorExample", "data": [{"y": 3.5825461088618984, "x": "Error Prevention", "e": 0.96452918311457403}, {"y": 4.0048920377867745, "x": "Visibility of System Status", "e": 0.21532335314612888}, {"y": 3.9349217638691321, "x": "Consistency and Standard", "e": 0.1521595464450598}, {"y": 4.2323968705547657, "x": "User control and Freedom", "e": 0.18086099376755968}, {"y": 4.4410512486170379, "x": "Match between System and the Real World", "e": 0.11736281777369589}, {"y": 4.2003668648405492, "x": "Help and Documentation", "e": 0.10354521141235926}, {"y": 4.2956215324636382, "x": "Recognition rather than recall", "e": 0.25890623246164085}, {"y": 3.9331983805668016, "x": "Aesthetic and Minimalist Design", "e": 0.15282916699961918}, {"y": 4.2847503373819169, "x": "Help Users Recognize, Diagnose, and Recover from Errors", "e": 0.074224021592443012}]}]}
var scratchpad1 = {'yMin' : 0, 'yMax' : 5.1, "yScale": "linear", "xScale": "ordinal", "comp": [{"className": ".comp.errorBar", "data": [{"y": 3.6281301544459441, "x": "Error Prevention", "e": 0.95869181865668551}, {"y": 4.1066412772478786, "x": "Visibility of System Status", "e": 0.22729364987668182}, {"y": 3.9631504569585068, "x": "Consistency and Standard", "e": 0.13098432138037527}, {"y": 4.2354266030736616, "x": "User control and Freedom", "e": 0.14793744171575196}, {"y": 4.4307661918884831, "x": "Match between System and the Real World", "e": 0.11278047143193183}, {"y": 4.1390005574216095, "x": "Help and Documentation", "e": 0.13160333339056784}, {"y": 4.3285555412748398, "x": "Recognition rather than recall", "e": 0.23907640465666452}, {"y": 4.020437338456964, "x": "Aesthetic and Minimalist Design", "e": 0.17554594997430181}, {"y": 4.3423759311359671, "x": "Help Users Recognize, Diagnose, and Recover from Errors", "e": 0.10155895676199114}], "type": "error"}], "main": [{"className": ".errorExample", "data": [{"y": 3.6281301544459441, "x": "Error Prevention", "e": 0.95869181865668551}, {"y": 4.1066412772478786, "x": "Visibility of System Status", "e": 0.22729364987668182}, {"y": 3.9631504569585068, "x": "Consistency and Standard", "e": 0.13098432138037527}, {"y": 4.2354266030736616, "x": "User control and Freedom", "e": 0.14793744171575196}, {"y": 4.4307661918884831, "x": "Match between System and the Real World", "e": 0.11278047143193183}, {"y": 4.1390005574216095, "x": "Help and Documentation", "e": 0.13160333339056784}, {"y": 4.3285555412748398, "x": "Recognition rather than recall", "e": 0.23907640465666452}, {"y": 4.020437338456964, "x": "Aesthetic and Minimalist Design", "e": 0.17554594997430181}, {"y": 4.3423759311359671, "x": "Help Users Recognize, Diagnose, and Recover from Errors", "e": 0.10155895676199114}]}]}

var errorBar = {
  enter: function (self, storage, className, data, callbacks) {
    var insertionPoint = xChart.visutils.getInsertionPoint(9),
      container,
      // Map each error bar into 3 points, so it's easier to draw as a single path
      // Converts each point to a triplet with y from (y - e) to (y + e)
      // It would be better to use the `preUpdateScale` method here,
      // but for this quick example, we're taking a shortcut :)
      eData = data.map(function (d) {
        d.data = d.data.map(function (d) {
          return [{x: d.x, y: d.y - d.e}, {x: d.x, y: d.y}, {x: d.x, y: d.y + d.e}];
        });
        return d;
      }),
      paths;

    // It's always a good idea to create containers for sets
    container = self._g.selectAll('.errorLine' + className)
      .data(eData, function (d) {
        return d.className;
      });

    // The insertionPoint is a special method that helps us insert this
    // vis at a particular z-index
    // In this case, we've chosen the highest point (above everything else)
    container.enter().insert('g', insertionPoint)
      .attr('class', function (d, i) {
        return 'errorLine' + className.replace(/\./g, ' ') +
          ' color' + i;
      });

    // Tell each path about its data
    // and ensure we reuse any previously drawn item
    paths = container.selectAll('path')
      .data(function (d) {
        return d.data;
      }, function (d) {
        return d[0].x;
      });

    paths.enter().insert('path')
      .style('opacity', 0)
      .attr('d', d3.svg.line()
        .x(function (d) {
          // We offset by half the rangeBand, because this is a bar chart
          return self.xScale(d.x) + self.xScale.rangeBand() / 2;
        })
        .y(function (d) { return self.yScale(d.y); })
      );

    storage.containers = container;
    storage.paths = paths;
  },
  update: function (self, storage, timing) {
    // This is mostly duplication to the d3.svg.line from the enter() method
    storage.paths.transition().duration(timing)
      .style('opacity', 1)
      .attr('d', d3.svg.line()
        .x(function (d) {
          return self.xScale(d.x) + self.xScale.rangeBand() / 2;
        })
        .y(function (d) { return self.yScale(d.y); })
      );
  },
  exit: function (self, storage, timing) {
    storage.paths.exit()
      .transition().duration(timing)
      .style('opacity', 0);
  },
  destroy: function (self, storage, timing) {
    storage.paths.transition().duration(timing)
      .style('opacity', 0)
      .remove();
  }
};


xChart.setVis('error', errorBar);

var options = {
  "tickFormatX": xformat,
  "tickFormatY": yformat
};
var first = new xChart('bar', andrew1, '#first', options);


//from http://stackoverflow.com/questions/196972/convert-string-to-title-case-with-javascript
function toTitleCase(str)
{
    return str.replace(/\w\S*/g, function(txt){return txt.charAt(0).toUpperCase() + txt.substr(1).toLowerCase();});
}

first_chart = {'book' : andrew1, 'conference' : conference1, 'cricket' : scratchpad1}
function resetData(experiment){
  first.setData(first_chart[experiment]);
  $('#header').text(toTitleCase(experiment) +  ' Website Results')

  $('#navbar li').attr('class', '');
  $('#' + experiment + '-nav').attr('class', 'active');
}

resetData('book');




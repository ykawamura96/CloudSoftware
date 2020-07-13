document.addEventListener('DOMContentLoaded',main,false);

function getRandomInt(max) {
  return Math.floor(Math.random() * Math.floor(max));
}

function fibc(n) {
    f =0; fn = 1; fnn = 1
    if( n == 0) return 0;
    if( n == 1) return 1;
    if( n == 2) return 1;
    for (let i = 0; i < n-2; i++) {
        fnn_tmp = fn + fnn; fn = fnn; f = fn; fnn = fnn_tmp
    }
    return fnn
}

function measure_time_simple(nfib, max_iter) {
    var times = [];
    var trans = [];
    var end = performance.now();
    for (let i = 0; i<max_iter; i++){
        var end2 = end;
        var start = performance.now();
        fibc(nfib);
        end = performance.now();
        times.push((end - start)/ 1000);
        trans.push((start - end2)/1000);
    }
    return [times, trans];
}

function measure_time_inc(nfib, max_iter) {
    var times = []
    for (let i = 0; i<nfib; i++){
        var start = performance.now();
        fibc(i);
        var end = performance.now();
        times.push((end - start)/ 1000);
    }
    return times;
}

function main() {
    target = document.getElementById("output");
    
    let y_simple = []; let y_inc = [];
    var max_iter = 50;
    var max_fib = 1000;
    var start = performance.now()
    console.log("start measuring time...");
    
    simple_ret = measure_time_simple(nfib=max_fib,
                                     times=max_iter);
    y_simple = simple_ret[0];
    trans_simple = simple_ret[1];
    y_inc = measure_time_inc(nfib=max_fib,
                             times=max_iter);
    var end = performance.now()

    var output  = "total time: " +  ((end-start) / 1000);
    target.innerHTML = output;
    
    let x_simple = [];
    for (let i = 0; i < max_iter; i++){
        x_simple.push(i);
    }
    let x_inc = [];
    for (let i = 0; i < max_fib; i++){
        x_inc.push(i);
    }
    var trace1 = {
        x: x_simple,
        y: y_simple,
        name: "time vs iter",
        type: 'scatter'
    };

    var trace2 = {
        x: x_inc,
        y: y_inc,
        name: "time vs fib(n)",
        xaxis: 'x2',
        yaxis: 'y2',
        type: 'scatter'
    };
    var trace3 = {
        x: x_simple,
        y: trans_simple,
        name: "time vs iter",
        xaxis: 'x3',
        yaxis: 'y3',
        type: 'scatter'
    };
    // var data = [trace1, trace2, trace3];
    var data = [trace1, trace2];

    var layout = {
        title: 'Scroll and Zoom',
        showlegend: true,
        grid: {rows: 1, columns: 2, pattern: 'independent'},
    };
    Plotly.newPlot('graph', data, layout, {scrollZoom: true});
}

import "performance";
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

function measure_time(nfib, times) {
    for (let i = 0; i<times; i++){
        const start = performance.now();
        fibc(ficb(nfib));
        const end = performance.now();
        console.log('time: %f', end - start);
    }
}

function main() {
    console.log("po")
    let ret = [];
    const max_iter = 10;
    const n_fib = 100;
    measure_time(nfib=100, times=10);
    for (let i = 0; i<11; i++){
        ret.push(fibc(i));
    }
    console.log(ret)
}

main();

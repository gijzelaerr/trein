
simms_config = file("simms.json")
pos = file("meerkat.itrf.txt")


process simms {
    container 'ares/simms'

    input:
    file simms_config
    file pos


    '''
    export INPUT=`pwd`
    export CONFIG=simms.json
    simms -jc simms.json
    '''
}


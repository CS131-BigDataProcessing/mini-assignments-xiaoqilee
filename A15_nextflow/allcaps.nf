#!/usr/bin/env nextflow

nextflow.enable.dsl=2

params.str = "Hello World"

workflow {
    input = Channel.value(params.str)
    result = toUpper(input)
    result.view()
}

process toUpper {
    input:
    val inputVal

    output:
    stdout()

    script:
    """
    echo "${inputVal}" | tr '[:lower:]' '[:upper:]'
    """
}

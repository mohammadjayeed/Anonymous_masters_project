The attached code provides library functions to read records from data files.
There are basically two reading mechanisms.
First, you can track the length of the records in their starting bytes.
Then you first determine the length by reading that starting bytes then read the record.
Second, you can use a record separator string when writing records in a file and during
reading read until you match the record separator. The library contains functions for
both modes of operation.
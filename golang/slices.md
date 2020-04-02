# Slices
{id: slices}

## Slice of an array
{id: slice-on-an-array}
{i: len}
{i: cap}

![](examples/slice-of-array/slice_of_array.go)
![](examples/slice-of-array/slice_of_array.out)

## Slice
{id: slice}
{i: slice}
{i: len}
{i: cap}

* You can view a slice to be just a very flexible array.
* Actually it is a slice of an array. A view on a section of the array.
* len - length
* cal - capacity

{aside}
The only difference you can see when we create a slice is that we don't explicitely say its size and we also don't put the 3 dots `...` in the square bracket.

There is also a `cap` function that returns the size of the underlying array.

We can access the elements of a slice using the postfix square-bracket notation. Just as with arrays.
{/aside}

![](examples/slice/slice.go)
![](examples/slice/slice.out)

## Change value in slice 
{id: slice-change-value}

![](examples/slice-change-value/slice_change_value.go)
![](examples/slice-change-value/slice_change_value.out)

## Slice Assign
{id: slice-assign}

* It is an alias to the other slice, same place in memory

{aside}
Unlike with arrays, when we assign a slice, we only assign the location of the slice in the memory. So if we change the content of one of the slices then the other one also sees the change. 
{/aside}

![](examples/slice-assign/slice_assign.go)
![](examples/slice-assign/slice_assign.out)


## Slice of a slice
{id: slice-of-slice}


![](examples/slice-of-slice/slice_of_slice.go)
![](examples/slice-of-slice/slice_of_slice.out)

* This would work on arrays as well: Slices of an array

## Slice append
{id: slice-append}
{i: append}

![](examples/slice-append/slice_append.go)
![](examples/slice-append/slice_append.out)

* Both the actual length and the capacity grew


* [slice internals](https://blog.golang.org/go-slices-usage-and-internals)
* [append to slice](https://tour.golang.org/moretypes/15)


## Remove last element of slice (pop)
{id: slice-remove-from-the-end}
{i: pop}

![](examples/slice-remove-last/slice_remove_last_element.go)
![](examples/slice-remove-last/slice_remove_last_element.out)

* The capacity remaind the same


## Remove first element of slice (shift, pop(0))
{id: remove-first-element-of-slice}
{i: shift}

![](examples/slice-shift/slice_shift.go)
![](examples/slice-shift/slice_shift.out)


## Pre-allocate capacity for slice with make
{id: pre-allocate-capacity-for-slice}
{i: make}

![](examples/slice-pre-allocate/slice_pre_allocate.go)
![](examples/slice-pre-allocate/slice_pre_allocate.out)

## For loop in slice - iterate over slice
{id: for-loop}
{i: range}
{i: for}

![](examples/loop-on-slice/loop_on_slice.go)
![](examples/loop-on-slice/loop_on_slice.out)

## for loop on values of slice (no index)
{id: for-values}

![](examples/for-values/for_values.go)


## Merge two slices
{id: merge-two-slices}
{i: ...}

![](examples/merge-slices/merge_slices.go)


## Find element in array or slice
{id: find-element-in-slice}

![](examples/find-element-in-slice/find_element_in_slice.go)
![](examples/find-element-in-slice/find_element_in_slice.out)

## Remove element of slice
{id: slice-remove-element}

![](examples/remove-element-from-slice/remove_element_from_slice.go)
![](examples/remove-element-from-slice/remove_element_from_slice.out)

## Weird merge slices
{id: weird-merge-slices}

* When we try to remove an element in the middle but assign to a new name.
* Avoid this mess!

![](examples/weird-merge-slices/weird_merge_slices.go)
![](examples/weird-merge-slices/weird_merge_slices.out)


## TODO: stack
{id: stack}

* see [lists](https://golang.org/pkg/container/list/)

## TODO: queue
{id: queue}

* see [lists](https://golang.org/pkg/container/list/)


## Exercise: count words
{id: exercise-count-words-slices}

![](examples/count-words-in-slices-skeleton/count_words_in_slices_skeleton.go)


## Exercise: Create a list of words from sentences
{id: exercise-create-list}

* Given a list of strings with words separated by spaces, create a single list of all the words.

![](examples/words-from-sentences-skeleton/words_from_sentences_skeleton.go)

## Exercise: Create a uniquie list of values
{id: exercise-unique-values}

Given a list of strings, create a list of unique values sorted by abc.

![](examples/unique-values-skeleton/unique_values_skeleton.go)

## Solution: count words
{id: solution-count-words-slices}

![](examples/count-words-in-slices/count_words_in_slices.go)

## Solution: Create a list of words from sentences
{id: solution-create-list}

TODO

## Solution: Create a uniquie list of values
{id: solution-unique-values}

TODO
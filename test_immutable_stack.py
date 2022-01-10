import pytest
from immutable_stack_implementation import EmptyStack


def test_if_push_on_an_empty_stack_does_not_modify_the_original_instance_but_returns_the_new_object():
    my_stack = EmptyStack()
    assert my_stack.push(1) is not my_stack


def test_if_push_on_a_non_empty_stack_does_not_modify_the_original_instance_but_returns_the_new_object():
    my_stack = EmptyStack()
    my_stack = my_stack.push(1)
    assert my_stack is not my_stack.push("x")


def test_if_pop_on_an_empty_stack_results_in_raising_a_value_error():
    my_stack = EmptyStack()
    with pytest.raises(ValueError):
        my_stack.pop()


def test_if_pop_on_a_non_empty_stack_results_in_returning_the_instance_of_previous_stack():
    first_stack = EmptyStack()
    second_stack = first_stack.push(1)
    assert second_stack.pop() is first_stack


def test_if_top_on_an_empty_stack_results_in_raising_a_value_error():
    my_stack = EmptyStack()
    with pytest.raises(ValueError):
        assert my_stack.top()


def test_if_top_on_a_non_empty_stack_results_in_the_last_pushed_value():
    my_stack = EmptyStack()
    my_stack = my_stack.push(1)
    assert my_stack.top() == 1








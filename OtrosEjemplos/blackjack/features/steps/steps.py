from behave import *
from twentyone import *

@given('a dealer')
def step_impl(context):
    context.dealer = Dealer()

## NEW STEP
@given('a hand {total:d}')
def step_impl(context, total):
    context.dealer = Dealer()
    context.total = total


@given('a {hand}')
def step_impl(context, hand):
    context.dealer = Dealer()
    context.dealer.hand = hand.split(',')

@when('the dealer determines a play')
def step_impl(context):
    context.dealer_play = context.dealer.determine_play(context.total)

@then('the dealer gives itself two cards')
def step_impl(context):
    assert (len(context.dealer.hand) == 2)


@then('the {total:d} is correct')
def step_impl(context, total):
    assert (context.dealer_total == total)

## NEW STEP
@then('the {play} is correct')
def step_impl(context, play):
    assert (context.dealer_play == play)
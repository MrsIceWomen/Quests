from main import show_quests

def test_show_quest():
    quests = [{'comment': 'first', 'amount': '1'},
              {'comment': 'second', 'amount': '2'},
              {'comment': 'third', 'amount': '3'}]
    show_quests(quests)
    assert True
    quests = []
    show_quests(quests)
    assert True



from main import quests_clear

def test_quest_clear():
    quests = [{'comment': 'first', 'amount': '1'},
              {'comment': 'second', 'amount': '2'},
              {'comment': 'third', 'amount': '1'}]
    quests_clear(quests)
    assert True
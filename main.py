DB_PATH = 'data/liuyao_db'
FILE_PATH = 'data/liuyao_knowledge'


if __name__ == '__main__':
    from function_tools.place import LiuyaoPlace,GuideComponent

    time_dict, msg_dict = GuideComponent(input('title'),input('coinNum'),input('Time'))
    model = LiuyaoPlace(time_dict, msg_dict)
    # model.place(True)
    model.place_to_html()
    print(''.join([str(i) for i in model.gua['coinNum']]))

    model.coinNum_change('reverse')
    model.coinNum_change('change')

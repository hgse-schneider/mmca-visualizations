from flask import Flask, render_template, jsonify, request

# install pyecharts
import numpy as np
import pandas as pd
import random

app = Flask(__name__)

# save start year and end year 
start_year = None
end_year = None


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


@app.route('/sankey')
def hello_world1():  # put application's code here
    return render_template('sankey.html')  # render html


@app.route('/relation')
def relation():
    return render_template('relation.html')  # render html


@app.route('/relation-cir')
def relation_cir():
    return render_template('relation-cir.html')  


@app.route('/tree')
def tree():  #
    return render_template('tree.html')


@app.route("/send_data", methods=["POST"])
def send_data():
    global start_year, end_year

   
    start_year = request.form.get("start_year")
    end_year = request.form.get("end_year")
    # print(start_year)
    # print(end_year)
    # sankey()
    

    return "Data received"


@app.route("/sankey1")
def sankey():
    # read data
    df = pd.read_excel('./outcome for sanky .xlsx')
    # df = pd.read_excel('./outcome for sanky .xlsx')
    # delete years 
    df.dropna(subset=['year'], inplace=True)

    # delete spaces
    df = df.applymap(lambda x: x.strip() if isinstance(x, str) else x)

    # delete empty lines 
    df = df.replace("\n", "", regex=True)

    # convert into small cases
    df = df.applymap(lambda x: x.lower() if isinstance(x, str) else x)

    # delete outcome one used once
    df = df.groupby('outcome').filter(lambda x: len(x) > 1)

    df['outcome_larger_category'] = df['outcome_larger_category'].replace('productproduct', 'product')

    # year 
    df['year'] = df['year'].astype(int)

    # print('输入开始年份')
    # start_year=int(input())
    # print('输入截止年份')
    # end_year=int(input())
    # start_year = request.args.get("start_year")  
    # end_year = request.args.get("end_year")  
    if start_year and end_year:
        df = df[df['year'].between(int(start_year), int(end_year))]


    nodes = []
    links = []

# copy paste and changed from other code 
    for index, row in df.iterrows():
        source = row['outcome_smaller_category']
        target = row['outcome_larger_category']
        outcome = row['outcome']
        value = 1

    
        if source == target:
            continue


        if {"name": source} not in nodes:
            nodes.append({"name": source})
        if {"name": target} not in nodes:
            nodes.append({"name": target})
        if {"name": outcome} not in nodes:
            nodes.append({"name": outcome})

    
        for link in links:
            if link['source'] == source and link['target'] == target:
            
                link['value'] += value
                break
        else:
            
            links.append({"source": source, "target": target, "value": value})

        #add outcome to outcome_smaller_category 
        for link in links:
            if link['source'] == outcome and link['target'] == source:  
                link['value'] += value
                break
        else:
            links.append({"source": outcome, "target": source, "value": value})

    # links = [link for link in links if link['source'] != link['target']]
    #
    # processed_data = {
    #     "nodes": nodes,
    #     "links": links
    # }
    linkss = []
    for i in links:
        if i['source'] == i['target']:
            continue
        else:
            linkss.append(i)

    processed_data = {
        "nodes": nodes,
        "links": linkss
    }

    return jsonify(processed_data)
    # print(jsonify(data))


@app.route("/relation1")
def relation1():
    df = pd.read_excel('outcome for sanky .xlsx') 
    df.dropna(subset=['year'], inplace=True)  
    df = df.applymap(lambda x: x.strip() if isinstance(x, str) else x)
    df = df.replace("\n", "", regex=True)   
    df = df.applymap(lambda x: x.lower() if isinstance(x, str) else x)
    df = df.groupby('outcome').filter(lambda x: len(x) > 1)
    df['outcome_larger_category'] = df['outcome_larger_category'].replace('productproduct', 'product')
    df['year'] = df['year'].astype(int)

    if start_year and end_year:
        df = df[df['year'].between(int(start_year), int(end_year))]

    nodes = []
    links = []
    categories = []

    def add_node(node_name, category):
        node_id = len(nodes)
        for node in nodes:
            if node['name'] == node_name:
                node['value'] += 1
                node['symbolSize'] = node['value']
                return
        new_node = {
            'id': node_id,
            'name': node_name,
            'value': 1,
            'symbolSize': 1,
            'category': category,
            'x': random.uniform(0, 100),
            'y': random.uniform(0, 100)
        }
        nodes.append(new_node)

    def add_link(source_name, target_name):
        source_id = None
        target_id = None
        for node in nodes:
            if node['name'] == source_name:
                source_id = node['id']
            elif node['name'] == target_name:
                target_id = node['id']
            if source_id is not None and target_id is not None:
                break
        if source_id is not None and target_id is not None:
            new_link = {
                'source': str(source_id),
                'target': str(target_id),

            }
            links.append(new_link)

    def add_category(category_name):
        for category in categories:
            if category['name'] == category_name:
                return
        new_category = {
            'name': category_name
        }
        categories.append(new_category)

    # 遍历数据，生成节点和链接
    for _, row in df.iterrows():
        outcome = row['outcome']
        smaller_category = row['outcome_smaller_category']
        larger_category = row['outcome_larger_category']

        add_node(outcome, 'outcome')
        add_node(smaller_category, 'outcome_smaller_category')
        add_node(larger_category, 'outcome_larger_category')

        add_link(outcome, smaller_category)
        add_link(outcome, larger_category)

    add_category('outcome')
    add_category('outcome_smaller_category')
    add_category('outcome_larger_category')

    linkss = []
    for i in links:
        if i['source'] == i['target']:
            continue
        else:
            linkss.append(i)

    graph_data = {
        'nodes': nodes,
        'links': linkss,
        'categories': categories
    }

    # print

    return jsonify(graph_data)


@app.route("/tree1")
def tree1():
    # 读取数据
    df = pd.read_excel('./outcome for sanky .xlsx')
    # df = pd.read_excel('./outcome for sanky .xlsx')
    # 删除缺失值所在的行
    df.dropna(subset=['year'], inplace=True)

    # 全部字段去除两端空格
    df = df.applymap(lambda x: x.strip() if isinstance(x, str) else x)

    # 去掉数据中的换行符（后面处理发现有隐藏的\n）
    df = df.replace("\n", "", regex=True)

    # 将字段列中的数据转换为小写
    df = df.applymap(lambda x: x.lower() if isinstance(x, str) else x)

    # 删除某一字段只有一个取值的行
    df = df.groupby('outcome').filter(lambda x: len(x) > 1)

    df['outcome_larger_category'] = df['outcome_larger_category'].replace('productproduct', 'product')

    # 将year字段的浮点型数据改为整数类型
    df['year'] = df['year'].astype(int)

    if start_year and end_year:
        df = df[df['year'].between(int(start_year), int(end_year))]

  
    data = {
        "name": "flare",
        "children": []
    }


    for index, row in df.iterrows():
        outcome = row['outcome']
        outcome_smaller_category = row['outcome_smaller_category']
        outcome_larger_category = row['outcome_larger_category']

    
        larger_category = next(
            (child for child in data['children'] if child['name'] == outcome_larger_category), None
        )

       
        if larger_category is None:
            larger_category = {
                "name": outcome_larger_category,
                "children": []
            }
            data['children'].append(larger_category)

       
        smaller_category = next(
            (child for child in larger_category['children'] if child['name'] == outcome_smaller_category), None
        )

      
        if smaller_category is None:
            smaller_category = {
                "name": outcome_smaller_category,
                "children": []
            }
            larger_category['children'].append(smaller_category)

       
        leaf_node = next(
            (child for child in smaller_category['children'] if child['name'] == outcome), None
        )

        
        if leaf_node is None:
            leaf_node = {
                "name": outcome,
                "value": 0
            }
            smaller_category['children'].append(leaf_node)

        leaf_node['value'] += 1

    return jsonify(data)


if __name__ == '__main__':
    app.run()

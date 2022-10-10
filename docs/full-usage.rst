.. highlight:: shell

=====
Full Usage
=====

|


To get aggregation on sentiment field on your twitter index, you can simply do:

.. code-block:: python

    >>> sentiments = esq.get_aggr_data(index='twitter', data_type='keyword/text',data_field='sentiment')
    >>> print(sentiments)
    [{'label': 'positive', 'value': 9}, {'label': 'neutral', 'value': 7}, {'label': 'negative', 'value': 1}]

| 

To get aggregation on stock field on your twitter index:

.. code-block:: python

    >>> stocks = esq.get_aggr_data(index='twitter-stream-stocks',data_type='keyword/text',data_field='stock')
    >>> print(stocks)
    [{'label': 'ITC', 'value': 2}, {'label': 'TOTAL', 'value': 2}, {'label': 'GALAXYSURF', 'value': 1}, {'label': 'HDFCBANK', 'value': 1}, {'label': 'RELIANCE', 'value': 1}, {'label': 'TAJGVK', 'value': 1}, {'label': 'TCI', 'value': 1}, {'label': 'ZOMATO', 'value': 1}]

| 

To get aggregation on stock field with stock label filter:

.. code-block:: python
    
    >>> filters = [{'filter_data_field': 'label_value','filter_field': 'stock','filter_value': 'ZOMATO'}]
    >>> stocks = esq.get_aggr_data(index='twitter-stream-stocks', data_type='keyword/text',data_field='stock',filters=filters)
    >>> print(stocks)
    [{'label': 'ZOMATO', 'value': 1}]

| 

To get aggregation on stock field with sentiment label filter:

.. code-block:: python
    
    >>> filters = [{'filter_data_field': 'label_value','filter_field': 'sentiment','filter_value': 'positive'}]
    >>> stocks = esq.get_aggr_data(index='twitter-stream-stocks',data_type='keyword/text',data_field='stock',filters=filters)
    >>> print(stocks)
    [{'label': 'TCI', 'value': 1}, {'label': 'ZOMATO', 'value': 1}]

| 

To get document of index with required fields:

.. code-block:: python
    
    >>> docs = esq.get_docs_data(index='twitter-stream-stocks',data_field=['id','stock','text','username'])
    >>> print(docs)
    [{'label': '1578656319657021441', 'value': {'id': 1578656319657021441, 'text': '@pankaj_prasoon @Ptcil @porinju @vikaskhemani @hiddengemsindia @MukulAg77304674 @utsav1711 Big leap. Hopefully will bcm marquee player with global footprint.\n\nLong way to go.', 'stock': ['TCI'], 'username': 'krishnblue'}}, {'label': '1578652887026401281', 'value': {'id': 1578652887026401281, 'text': 'RT @CNBCTV18News: #InsideOut | U Shekhar, Promoter &amp; MD of Galaxy Surfactants explains the oleochemicals business, how China +1 strategy im…', 'stock': ['GALAXYSURF'], 'username': 'sonalbhutra'}}, {'label': '1578608126198448129', 'value': {'id': 1578608126198448129, 'text': 'RT @sbikh: Just met @deepigoyal and the @zomato team. Delighted to learn that all senior managers including Deepinder don a red Zomato tee,…', 'stock': ['ZOMATO'], 'username': 'varinder_bansal'}}, {'label': '1578605966786170880', 'value': {'id': 1578605966786170880, 'text': '#TAJGVK - #TAJGVK chart on @TradingView https://t.co/WB0MM6JsxG', 'stock': ['TAJGVK'], 'username': 'krishnakhanna'}}, {'label': '1578605345361956864', 'value': {'id': 1578605345361956864, 'text': 'RT @ipo_mantra: Final figures in Electronic Mart IPO\n\nQIB: 178.6X\nHNI (Big): 69.7X\nHNI (Small): 61.5X\nRetail: 20.8X\nTOTAL: 75.8X\n\nAllotment…', 'stock': ['TOTAL'], 'username': 'ipo_mantra'}}, {'label': '1578605244333686784', 'value': {'id': 1578605244333686784, 'text': 'RT @ipo_mantra: Final figures in Electronic Mart IPO\n\nQIB: 178.6X\nHNI (Big): 69.7X\nHNI (Small): 61.5X\nRetail: 20.8X\nTOTAL: 75.8X\n\nAllotment…', 'stock': ['TOTAL'], 'username': 'ipo_mantra'}}]

| 

To get single doc using id in filters, can mention required fields in array or pass it empty:

.. code-block:: python
    
    >>> filters = [{'filter_data_field': 'label_value','filter_field': 'id','filter_value': '1578608126198448129'}]
    >>> doc = esq.get_docs_data(index='twitter-stream-stocks',data_field=['id','stock','text','username'],filters=filters)
    >>> print(doc)
    [{'id': 1578608126198448129, 'text': 'RT @sbikh: Just met @deepigoyal and the @zomato team. Delighted to learn that all senior managers including Deepinder don a red Zomato tee,…', 'stock': ['ZOMATO'], 'username': 'varinder_bansal'}}]

| 

To get all docs from index you can mention size, if fields not mentioned, it will return all fields stored in index

.. code-block:: python
    
    >>> docs = esq.get_docs_data(index='twitter-stream-stocks')
    >>> print(docs)
    [{'label': '1578678257754730496', 'value': {'sentiment': 'bullish', 'hashtags': [], 'id_str': 1578678257754730496, 'mentions': ['Shrikan49162239'], 'id': 1578678257754730496, 'text': '@Shrikan49162239 Better go for Reliance', 'created_utc': 1665221201000, 'stock': ['RELIANCE'], 'user': {'followers_count': 214822, 'name': 'Sandeep Jain Tradeswift', 'verified': False, 'created_at': 1497350069000, 'id': 874575696189771777}, 'tweet_type': 'Tweet', 'username': 'SandeepKrJainTS'}}, {'label': '1578656319657021441', 'value': {'sentiment': 'bullish', 'hashtags': [], 'id_str': 1578656319657021441, 'mentions': ['pankaj_prasoon', 'Ptcil', 'porinju', 'vikaskhemani', 'hiddengemsindia', 'MukulAg77304674', 'utsav1711'], 'id': 1578656319657021441, 'text': '@pankaj_prasoon @Ptcil @porinju @vikaskhemani @hiddengemsindia @MukulAg77304674 @utsav1711 Big leap. Hopefully will bcm marquee player with global footprint.\n\nLong way to go.', 'created_utc': 1665215971000, 'stock': ['TCI'], 'user': {'followers_count': 49510, 'name': 'Krishna Agrawal', 'verified': False, 'created_at': 1422125373000, 'id': 2995027303}, 'tweet_type': 'Tweet', 'username': 'krishnblue'}}, {'label': '1578652887026401281', 'value': {'sentiment': 'neutral', 'hashtags': ['InsideOut'], 'id_str': 1578652887026401281, 'mentions': ['CNBCTV18News'], 'id': 1578652887026401281, 'text': 'RT @CNBCTV18News: #InsideOut | U Shekhar, Promoter &amp; MD of Galaxy Surfactants explains the oleochemicals business, how China +1 strategy im…', 'created_utc': 1665215152000, 'stock': ['GALAXYSURF'], 'user': {'followers_count': 48522, 'name': 'Sonal Bhutra', 'verified': True, 'created_at': 1458843992000, 'id': 713069501504327680}, 'tweet_type': 'Tweet', 'username': 'sonalbhutra'}}, {'label': '1578608126198448129', 'value': {'sentiment': 'bullish', 'hashtags': [], 'id_str': 1578608126198448129, 'mentions': ['sbikh', 'deepigoyal', 'zomato'], 'id': 1578608126198448129, 'text': 'RT @sbikh: Just met @deepigoyal and the @zomato team. Delighted to learn that all senior managers including Deepinder don a red Zomato tee,…', 'created_utc': 1665204481000, 'stock': ['ZOMATO'], 'user': {'followers_count': 344873, 'name': 'Varinder Bansal 🇮🇳', 'verified': True, 'created_at': 1328627872000, 'id': 485769605}, 'tweet_type': 'Tweet', 'username': 'varinder_bansal'}}, {'label': '1578605966786170880', 'value': {'sentiment': 'neutral', 'hashtags': ['TAJGVK', 'TAJGVK'], 'id_str': 1578605966786170880, 'mentions': ['tradingview'], 'id': 1578605966786170880, 'text': '#TAJGVK - #TAJGVK chart on @TradingView https://t.co/WB0MM6JsxG', 'created_utc': 1665203966000, 'stock': ['TAJGVK'], 'user': {'followers_count': 12552, 'name': 'kkonline.org', 'verified': False, 'created_at': 1251871956000, 'id': 70897812}, 'tweet_type': 'Tweet', 'username': 'krishnakhanna'}}, {'label': '1578605345361956864', 'value': {'sentiment': 'neutral', 'hashtags': [], 'id_str': 1578605345361956864, 'mentions': ['ipo_mantra'], 'id': 1578605345361956864, 'text': 'RT @ipo_mantra: Final figures in Electronic Mart IPO\n\nQIB: 178.6X\nHNI (Big): 69.7X\nHNI (Small): 61.5X\nRetail: 20.8X\nTOTAL: 75.8X\n\nAllotment…', 'created_utc': 1665203818000, 'stock': ['TOTAL'], 'user': {'followers_count': 298354, 'name': 'R.K.', 'verified': False, 'created_at': 1464593979000, 'id': 737186694559113216}, 'tweet_type': 'Tweet', 'username': 'ipo_mantra'}}, {'label': '1578605244333686784', 'value': {'sentiment': 'neutral', 'hashtags': [], 'id_str': 1578605244333686784, 'mentions': ['ipo_mantra'], 'id': 1578605244333686784, 'text': 'RT @ipo_mantra: Final figures in Electronic Mart IPO\n\nQIB: 178.6X\nHNI (Big): 69.7X\nHNI (Small): 61.5X\nRetail: 20.8X\nTOTAL: 75.8X\n\nAllotment…', 'created_utc': 1665203793000, 'stock': ['TOTAL'], 'user': {'followers_count': 298354, 'name': 'R.K.', 'verified': False, 'created_at': 1464593979000, 'id': 737186694559113216}, 'tweet_type': 'Tweet', 'username': 'ipo_mantra'}}, {'label': '1578604719148216320', 'value': {'sentiment': 'neutral', 'hashtags': ['ITC', 'RELIANCE'], 'id_str': 1578604719148216320, 'mentions': [], 'id': 1578604719148216320, 'text': 'Testing rise of #ITC #RELIANCE', 'created_utc': 1665203668000, 'stock': ['ITC', 'RELIANCE'], 'user': {'followers_count': 47, 'name': 'Shuvam Agrawal', 'verified': False, 'created_at': 1288805890000, 'id': 211585197}, 'tweet_type': 'Tweet', 'username': 'shuvam91'}}, {'label': '1578462199692947456', 'value': {'sentiment': 'neutral', 'hashtags': [], 'id_str': 1578462199692947456, 'mentions': [], 'id': 1578462199692947456, 'text': 'test $ITC $HDFCBANK', 'created_utc': 1665169689000, 'stock': ['ITC', 'HDFCBANK'], 'user': {'followers_count': 25, 'name': 'Vikash Bajaj', 'verified': False, 'created_at': 1337137475000, 'id': 581464808}, 'tweet_type': 'Tweet', 'username': 'bajaj_vikash'}}]


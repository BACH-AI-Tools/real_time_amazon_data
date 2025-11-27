# Real Time Amazon Data MCP Server

[English](./README_EN.md) | 简体中文 | [繁體中文](./README_ZH-TW.md)

## 🚀 使用 EMCP 平台快速体验

**[EMCP](https://sit-emcp.kaleido.guru)** 是一个强大的 MCP 服务器管理平台，让您无需手动配置即可快速使用各种 MCP 服务器！

### 快速开始：

1. 🌐 访问 **[EMCP 平台](https://sit-emcp.kaleido.guru)**
2. 📝 注册并登录账号
3. 🎯 进入 **MCP 广场**，浏览所有可用的 MCP 服务器
4. 🔍 搜索或找到本服务器（`bach-real_time_amazon_data`）
5. 🎉 点击 **"安装 MCP"** 按钮
6. ✅ 完成！即可在您的应用中使用

### EMCP 平台优势：

- ✨ **零配置**：无需手动编辑配置文件
- 🎨 **可视化管理**：图形界面轻松管理所有 MCP 服务器
- 🔐 **安全可靠**：统一管理 API 密钥和认证信息
- 🚀 **一键安装**：MCP 广场提供丰富的服务器选择
- 📊 **使用统计**：实时查看服务调用情况

立即访问 **[EMCP 平台](https://sit-emcp.kaleido.guru)** 开始您的 MCP 之旅！


---

## 简介

这是一个 MCP 服务器，用于访问 Real Time Amazon Data API。

- **PyPI 包名**: `bach-real_time_amazon_data`
- **版本**: 2.0.0
- **传输协议**: stdio


## 安装

### 从 PyPI 安装:

```bash
pip install bach-real_time_amazon_data
```

### 从源码安装:

```bash
pip install -e .
```

## 运行

### 方式 1: 使用 uvx（推荐，无需安装）

```bash
# 运行（uvx 会自动安装并运行）
uvx --from bach-real_time_amazon_data bach_real_time_amazon_data

# 或指定版本
uvx --from bach-real_time_amazon_data@latest bach_real_time_amazon_data
```

### 方式 2: 直接运行（开发模式）

```bash
python server.py
```

### 方式 3: 安装后作为命令运行

```bash
# 安装
pip install bach-real_time_amazon_data

# 运行（命令名使用下划线）
bach_real_time_amazon_data
```

## 配置

### API 认证

此 API 需要认证。请设置环境变量:

```bash
export API_KEY="your_api_key_here"
```

### 环境变量

| 变量名 | 说明 | 必需 |
|--------|------|------|
| `API_KEY` | API 密钥 | 是 |




### 在 Claude Desktop 中使用

编辑 Claude Desktop 配置文件 `claude_desktop_config.json`:


```json
{
  "mcpServers": {
    "real_time_amazon_data": {
      "command": "uvx",
      "args": ["--from", "bach-real_time_amazon_data", "bach_real_time_amazon_data"],
      "env": {
        "API_KEY": "your_api_key_here"
      }
    }
  }
}
```

**注意**: 请将 `E:\path\to\real_time_amazon_data\server.py` 替换为实际的服务器文件路径。


## 可用工具

此服务器提供以下工具:


### `influencer_post_products`

Get the list of products related to a \

**端点**: `GET /influencer-post-products`


**参数**:

- `influencer_name` (string) *必需*: Example value: madison.lecroy

- `post_id` (string) *必需*: Influencer Post ID (e.g. amzn1.ideas.1N84PQ3CI4NW0) of the list post for which to get product items (only posts with post_type=List are allowed).

- `cursor` (string): Set the cursor value from the response of the previous call to get the next results page.

- `language` (string): The language of the results. In case not specified, results will be returned in the default domain language. Supported languages per country: US: en_US, es_US AU: en_AU BR: pt_BR CA: en_CA, fr_CA FR: fr_FR, en_GB DE: de_DE, en_GB, cs_CZ, nl_NL, pl_PL, tr_TR, da_DK IN: en_IN, hi_IN, ta_IN, te_IN, kn_IN, ml_IN, bn_IN, mr_IN IT: it_IT, en_GB MX: es_MX NL: nl_NL, en_GB SG: en_SG ES: es_ES, pt_PT, en_GB TR: tr_TR AE: en_AE, ar_AE GB: en_GB JP: ja_JP, en_US, zh_CN SA: ar_AE, en_AE PL: pl_PL SE: sv_SE,



---


### `product_reviews`

Get and paginate through product reviews on Amazon using a logged in user cookie string. Each page contains up to 10 reviews.

**端点**: `GET /product-reviews`


**参数**:

- `asin` (string) *必需*: Product asin for which to get reviews.

- `country` (string): Sets the Amazon domain, marketplace country, language and currency. Default: US Allowed values: US, AU, BR, CA, CN, FR, DE, IN, IT, MX, NL, SG, ES, TR, AE, GB, JP, SA, PL, SE, BE, EG, ZA, IE

- `page` (string): Results page to return. Default: 1

- `sort_by` (string): Return reviews in a specific sort order. Default: TOP_REVIEWS Allowed values: TOP_REVIEWS, MOST_RECENT

- `star_rating` (string): Only return reviews with a specific star rating. Default: ALL Allowed values: ALL, 5_STARS, 4_STARS, 3_STARS, 2_STARS, 1_STARS, POSITIVE, CRITICAL

- `verified_purchases_only` (string): Example value: 

- `images_or_videos_only` (string): Example value: 

- `current_format_only` (string): Example value: 

- `query` (string): Find reviews matching a search query.

- `fields` (string): A comma separated list of review fields to include in the response (field projection). By default all fields are returned. Example: review_title,review_images,review_date,country

- `language` (string): The language of the results. In case not specified, results will be returned in the default domain language. Supported languages per country: US: en_US, es_US AU: en_AU BR: pt_BR CA: en_CA, fr_CA FR: fr_FR, en_GB DE: de_DE, en_GB, cs_CZ, nl_NL, pl_PL, tr_TR, da_DK IN: en_IN, hi_IN, ta_IN, te_IN, kn_IN, ml_IN, bn_IN, mr_IN IT: it_IT, en_GB MX: es_MX NL: nl_NL, en_GB SG: en_SG ES: es_ES, pt_PT, en_GB TR: tr_TR AE: en_AE, ar_AE GB: en_GB JP: ja_JP, en_US, zh_CN SA: ar_AE, en_AE PL: pl_PL SE: sv_SE,



---


### `product_category_list`

Get Amazon product categories per country / Amazon domain (for use with the \

**端点**: `GET /product-category-list`


**参数**:

- `country` (string): Sets the Amazon domain, marketplace country, language and currency. Default: US Allowed values: US, AU, BR, CA, CN, FR, DE, IN, IT, MX, NL, SG, ES, TR, AE, GB, JP, SA, PL, SE, BE, EG, ZA, IE



---


### `asin_to_gtin`

Convert an Amazon ASIN to GTIN / EAN / UPS identifiers. Valid values for `type` are `EAN-13`, `UPC`, or `ISBN`.

**端点**: `GET /asin-to-gtin`


**参数**:

- `asin` (string) *必需*: Amazon product ASIN to convert.

- `country` (string): Sets the Amazon domain, marketplace country, language and currency. Default: US Allowed values: US, AU, BR, CA, CN, FR, DE, IN, IT, MX, NL, SG, ES, TR, AE, GB, JP, SA, PL, SE, BE, EG, ZA, IE



---


### `influencer_posts`

Get all Amazon Influencer posts with pagination support.

**端点**: `GET /influencer-posts`


**参数**:

- `influencer_name` (string) *必需*: The Amazon Influencer name for which to get posts

- `country` (string): Sets the Amazon domain, marketplace country, language and currency. Default: US Allowed values: US, AU, BR, CA, CN, FR, DE, IN, IT, MX, NL, SG, ES, TR, AE, GB, JP, SA, PL, SE, BE, EG, ZA, IE

- `scope` (string): Return the results in a specific scope. Default: ALL Allowed values: ALL, IDEA_LISTS, PHOTOS, VIDEOS

- `query` (string): Find posts matching a search query.

- `cursor` (string): A cursor to get the next set of results, it can be used for for paging purposes. Note: the cursor value for the next set of results is returned by this endpoint under data.cursor.

- `limit` (string): Maximum number of posts to return. Default: 20 Allowed values: 1-100

- `language` (string): The language of the results. In case not specified, results will be returned in the default domain language. Supported languages per country: US: en_US, es_US AU: en_AU BR: pt_BR CA: en_CA, fr_CA FR: fr_FR, en_GB DE: de_DE, en_GB, cs_CZ, nl_NL, pl_PL, tr_TR, da_DK IN: en_IN, hi_IN, ta_IN, te_IN, kn_IN, ml_IN, bn_IN, mr_IN IT: it_IT, en_GB MX: es_MX NL: nl_NL, en_GB SG: en_SG ES: es_ES, pt_PT, en_GB TR: tr_TR AE: en_AE, ar_AE GB: en_GB JP: ja_JP, en_US, zh_CN SA: ar_AE, en_AE PL: pl_PL SE: sv_SE,

- `fields` (string): A comma separated list of influencer post fields to include in the response (field projection). By default all fields are returned. Example: post_url,post_title,is_pinned,video_duration



---


### `promo_code_details`

Get the products offered by an Amazon promo code.

**端点**: `GET /promo-code-details`


**参数**:

- `promo_code` (string) *必需*: Promo code for which to get products. The promo code can be extracted from the /promocode Amazon URL. For example the promo code for https://www.amazon.com/promocode/A31M10S4V50SOU is A31M10S4V50SOU.

- `country` (string): Sets the Amazon domain, marketplace country, language and currency. Default: US Allowed values: US, AU, BR, CA, CN, FR, DE, IN, IT, MX, NL, SG, ES, TR, AE, GB, JP, SA, PL, SE, BE, EG, ZA, IE

- `language` (string): The language of the results. In case not specified, results will be returned in the default domain language. Supported languages per country: US: en_US, es_US AU: en_AU BR: pt_BR CA: en_CA, fr_CA FR: fr_FR, en_GB DE: de_DE, en_GB, cs_CZ, nl_NL, pl_PL, tr_TR, da_DK IN: en_IN, hi_IN, ta_IN, te_IN, kn_IN, ml_IN, bn_IN, mr_IN IT: it_IT, en_GB MX: es_MX NL: nl_NL, en_GB SG: en_SG ES: es_ES, pt_PT, en_GB TR: tr_TR AE: en_AE, ar_AE GB: en_GB JP: ja_JP, en_US, zh_CN SA: ar_AE, en_AE PL: pl_PL SE: sv_SE,



---


### `deal_products`

Get the products of a specific deal by Deal ID. Supports pagination using the *page* parameter. For now, only works for MULTI_ITEM deals with no canonical_deal_url (i.e. when deal_url is in the form of *https://amazon_domain/deal/deal_id*).

**端点**: `GET /deal-products`


**参数**:

- `deal_id` (string) *必需*: Deal ID of the deal to fetch

- `country` (string): Sets the Amazon domain, marketplace country, language and currency. Default: US Allowed values: US, AU, BR, CA, CN, FR, DE, IN, IT, MX, NL, SG, ES, TR, AE, GB, JP, SA, PL, SE, BE, EG, ZA, IE

- `sort_by` (string): Return products in a specific order. Default: FEATURED Allowed values: FEATURED, LOWEST_PRICE, HIGHEST_PRICE, REVIEWS, NEWEST, BEST_SELLERS

- `page` (string): Results page to return. Default: 1

- `language` (string): The language of the results. In case not specified, results will be returned in the default domain language. Supported languages per country: US: en_US, es_US AU: en_AU BR: pt_BR CA: en_CA, fr_CA FR: fr_FR, en_GB DE: de_DE, en_GB, cs_CZ, nl_NL, pl_PL, tr_TR, da_DK IN: en_IN, hi_IN, ta_IN, te_IN, kn_IN, ml_IN, bn_IN, mr_IN IT: it_IT, en_GB MX: es_MX NL: nl_NL, en_GB SG: en_SG ES: es_ES, pt_PT, en_GB TR: tr_TR AE: en_AE, ar_AE GB: en_GB JP: ja_JP, en_US, zh_CN SA: ar_AE, en_AE PL: pl_PL SE: sv_SE,

- `fields` (string): A comma separated list of deal product fields to include in the response (field projection). By default all fields are returned. Example: product_title,deal_price,deal_badge



---


### `best_sellers`

Get Amazon Best Sellers, including prices, ratings, rank and more data points available on Amazon Best Sellers listings. Supports all Amazon Best Seller list types using the `type` parameter: **Best Sellers**, **New Releases**, **Movers \u0026 Shakers**, **Most Wished For**, **Gift Ideas**.

**端点**: `GET /best-sellers`


**参数**:

- `category` (string) *必需*: Best sellers category to return products for. Supports top level best sellers categories (e.g. software). In addition, subcategories / category path can be specified as well, separated by / (e.g. software/229535) - this can be seen in best sellers URLs, e.g. https://www.amazon.com/Best-Sellers-Software-Business-Office/zgbs/software/229535. Examples: software software/229535

- `type` (string): Type of Best Seller list to return. Default: BEST_SELLERS Allowed values: BEST_SELLERS, GIFT_IDEAS, MOST_WISHED_FOR, MOVERS_AND_SHAKERS, NEW_RELEASES

- `page` (string): Results page to return. Default: 1

- `country` (string): Sets the Amazon domain, marketplace country, language and currency. Default: US Allowed values: US, AU, BR, CA, CN, FR, DE, IN, IT, MX, NL, SG, ES, TR, AE, GB, JP, SA, PL, SE, BE, EG, ZA, IE

- `language` (string): The language of the results. In case not specified, results will be returned in the default domain language. Supported languages per country: US: en_US, es_US AU: en_AU BR: pt_BR CA: en_CA, fr_CA FR: fr_FR, en_GB DE: de_DE, en_GB, cs_CZ, nl_NL, pl_PL, tr_TR, da_DK IN: en_IN, hi_IN, ta_IN, te_IN, kn_IN, ml_IN, bn_IN, mr_IN IT: it_IT, en_GB MX: es_MX NL: nl_NL, en_GB SG: en_SG ES: es_ES, pt_PT, en_GB TR: tr_TR AE: en_AE, ar_AE GB: en_GB JP: ja_JP, en_US, zh_CN SA: ar_AE, en_AE PL: pl_PL SE: sv_SE,

- `fields` (string): A comma separated list of product fields to include in the response (field projection). By default all fields are returned. Example: product_title,product_url,product_photo



---


### `seller_products`

Get and paginate through the products sold by an Amazon Seller

**端点**: `GET /seller-products`


**参数**:

- `seller_id` (string) *必需*: The Amazon Seller ID for which to get seller product listings

- `country` (string): Sets the Amazon domain, marketplace country, language and currency. Default: US Allowed values: US, AU, BR, CA, CN, FR, DE, IN, IT, MX, NL, SG, ES, TR, AE, GB, JP, SA, PL, SE, BE, EG, ZA, IE

- `page` (string): The page of seller products results to retrieve Seller products result page to retrieve. Default: 1

- `sort_by` (string): Return the results in a specific sort order. Default: RELEVANCE Allowed values: RELEVANCE, LOWEST_PRICE, HIGHEST_PRICE, REVIEWS, NEWEST, BEST_SELLERS

- `language` (string): The language of the results. In case not specified, results will be returned in the default domain language. Supported languages per country: US: en_US, es_US AU: en_AU BR: pt_BR CA: en_CA, fr_CA FR: fr_FR, en_GB DE: de_DE, en_GB, cs_CZ, nl_NL, pl_PL, tr_TR, da_DK IN: en_IN, hi_IN, ta_IN, te_IN, kn_IN, ml_IN, bn_IN, mr_IN IT: it_IT, en_GB MX: es_MX NL: nl_NL, en_GB SG: en_SG ES: es_ES, pt_PT, en_GB TR: tr_TR AE: en_AE, ar_AE GB: en_GB JP: ja_JP, en_US, zh_CN SA: ar_AE, en_AE PL: pl_PL SE: sv_SE,

- `fields` (string): A comma separated list of seller product fields to include in the response (field projection). By default all fields are returned. Example: product_price,product_url,is_prime



---


### `seller_reviews`

Get and paginate through Amazon Seller reviews / feedback as shown on the Seller profile page (e.g. https://www.amazon.com/sp?seller=A1D09S7Q0OD6TH). Each page contains up to 5 reviews.

**端点**: `GET /seller-reviews`


**参数**:

- `seller_id` (string) *必需*: The Amazon Seller ID for which to get seller reviews

- `country` (string): Sets the Amazon domain, marketplace country, language and currency. Default: US Allowed values: US, AU, BR, CA, CN, FR, DE, IN, IT, MX, NL, SG, ES, TR, AE, GB, JP, SA, PL, SE, BE, EG, ZA, IE

- `star_rating` (string): Only return reviews with a specific star rating or positive / negative sentiment. Default: ALL Allowed values: ALL, 5_STARS, 4_STARS, 3_STARS, 2_STARS, 1_STARS, POSITIVE, CRITICAL

- `page` (string): The page of seller feedback results to retrieve. Default: 1

- `language` (string): The language of the results. In case not specified, results will be returned in the default domain language. Supported languages per country: US: en_US, es_US AU: en_AU BR: pt_BR CA: en_CA, fr_CA FR: fr_FR, en_GB DE: de_DE, en_GB, cs_CZ, nl_NL, pl_PL, tr_TR, da_DK IN: en_IN, hi_IN, ta_IN, te_IN, kn_IN, ml_IN, bn_IN, mr_IN IT: it_IT, en_GB MX: es_MX NL: nl_NL, en_GB SG: en_SG ES: es_ES, pt_PT, en_GB TR: tr_TR AE: en_AE, ar_AE GB: en_GB JP: ja_JP, en_US, zh_CN SA: ar_AE, en_AE PL: pl_PL SE: sv_SE,

- `fields` (string): A comma separated list of seller review fields to include in the response (field projection). By default all fields are returned. Example: review_star_rating,review_date



---


### `product_review_details`

Get the details of a specific product review by id

**端点**: `GET /product-review-details`


**参数**:

- `review_id` (string) *必需*: The id of the product review for which to get details.

- `country` (string): Sets the Amazon domain, marketplace country, language and currency. Default: US Allowed values: US, AU, BR, CA, CN, FR, DE, IN, IT, MX, NL, SG, ES, TR, AE, GB, JP, SA, PL, SE, BE, EG, ZA, IE

- `language` (string): The language of the results. In case not specified, results will be returned in the default domain language. Supported languages per country: US: en_US, es_US AU: en_AU BR: pt_BR CA: en_CA, fr_CA FR: fr_FR, en_GB DE: de_DE, en_GB, cs_CZ, nl_NL, pl_PL, tr_TR, da_DK IN: en_IN, hi_IN, ta_IN, te_IN, kn_IN, ml_IN, bn_IN, mr_IN IT: it_IT, en_GB MX: es_MX NL: nl_NL, en_GB SG: en_SG ES: es_ES, pt_PT, en_GB TR: tr_TR AE: en_AE, ar_AE GB: en_GB JP: ja_JP, en_US, zh_CN SA: ar_AE, en_AE PL: pl_PL SE: sv_SE,

- `fields` (string): A comma separated list of review fields to include in the response (field projection). By default all fields are returned. Example: review_title,review_images,review_date,country



---


### `product_details`

Get extensive Amazon product details and information available on the Amazon product page by asin, including title, price data, ratings data, local and global top reviews, photos, product details (brand, weight, package size, model, etc) product variations (colors, sizes, flavors, etc), and many other data points. Here's an example product page: [https://www.amazon.com/dp/B0CMZFCQ6D](https://www.amazon.com/dp/B0CMZFCQ6D).

**端点**: `GET /product-details`


**参数**:

- `asin` (string) *必需*: Product ASIN for which to get details. Supports batching of up to 10 ASINs in a single request, separated by comma. Examples: B08BHXG144 B08PPDJWC8,B07ZPKBL9V,B08BHXG144 Note that each ASIN in a batch request is counted as a single request against the plan quota.

- `country` (string): Sets the Amazon domain, marketplace country, language and currency. Default: US Allowed values: US, AU, BR, CA, CN, FR, DE, IN, IT, MX, NL, SG, ES, TR, AE, GB, JP, SA, PL, SE, BE, EG, ZA, IE

- `autoselect_variant` (string): Example value: 

- `more_info_query` (string): A query to search and get more info about the product as part of Product Information, Customer Q&As, and Customer Reviews.

- `language` (string): The language of the results. In case not specified, results will be returned in the default domain language. Supported languages per country: US: en_US, es_US AU: en_AU BR: pt_BR CA: en_CA, fr_CA FR: fr_FR, en_GB DE: de_DE, en_GB, cs_CZ, nl_NL, pl_PL, tr_TR, da_DK IN: en_IN, hi_IN, ta_IN, te_IN, kn_IN, ml_IN, bn_IN, mr_IN IT: it_IT, en_GB MX: es_MX NL: nl_NL, en_GB SG: en_SG ES: es_ES, pt_PT, en_GB TR: tr_TR AE: en_AE, ar_AE GB: en_GB JP: ja_JP, en_US, zh_CN SA: ar_AE, en_AE PL: pl_PL SE: sv_SE,

- `fields` (string): A comma separated list of product fields to include in the response (field projection). By default all fields are returned. Example: product_price,product_url,is_best_seller,sales_volume



---


### `product_offers`

Get all Amazon product details as available via the Product Details endpoint with an additional `offers` array containing product offers (The first offer in the array is the pinned offer returned by the **Search** endpoint). Supports pagination using the `page` and `limit` parameters.

**端点**: `GET /product-offers`


**参数**:

- `asin` (string) *必需*: Product ASIN for which to get offers. Supports batching of up to 10 ASINs in a single request, separated by comma. Example: B08PPDJWC8,B07ZPKBL9V,B08BHXG144 Note that each ASIN in a batch request is counted as a single request against the plan quota.

- `country` (string): Sets the Amazon domain, marketplace country, language and currency. Default: US Allowed values: US, AU, BR, CA, CN, FR, DE, IN, IT, MX, NL, SG, ES, TR, AE, GB, JP, SA, PL, SE, BE, EG, ZA, IE

- `product_condition` (string): Find products in specific conditions, specified as a comma delimited list of the following values: NEW, USED_LIKE_NEW, USED_VERY_GOOD, USED_GOOD, USED_ACCEPTABLE. Default: NEW, USED_LIKE_NEW, USED_VERY_GOOD, USED_GOOD, USED_ACCEPTABLE Examples: NEW,USED_LIKE_NEW USED_VERY_GOOD,USED_GOOD,USED_LIKE_NEW

- `delivery` (string): Find products with specific delivery option, specified as a comma delimited list of the following values: PRIME_ELIGIBLE,FREE_DELIVERY. Examples: FREE_DELIVERY PRIME_ELIGIBLE,FREE_DELIVERY

- `autoselect_variant` (string): Example value: 

- `limit` (string): Maximum number of offers to return. Default: 100

- `page` (string): Results page to return. Default: 1

- `language` (string): The language of the results. In case not specified, results will be returned in the default domain language. Supported languages per country: US: en_US, es_US AU: en_AU BR: pt_BR CA: en_CA, fr_CA FR: fr_FR, en_GB DE: de_DE, en_GB, cs_CZ, nl_NL, pl_PL, tr_TR, da_DK IN: en_IN, hi_IN, ta_IN, te_IN, kn_IN, ml_IN, bn_IN, mr_IN IT: it_IT, en_GB MX: es_MX NL: nl_NL, en_GB SG: en_SG ES: es_ES, pt_PT, en_GB TR: tr_TR AE: en_AE, ar_AE GB: en_GB JP: ja_JP, en_US, zh_CN SA: ar_AE, en_AE PL: pl_PL SE: sv_SE,

- `fields` (string): A comma separated list of product and offer fields to include in the response (field projection). By default all fields are returned. Example: product_price,product_information,product_condition,ships_from



---


### `influencer_profile`

Get Amazon Influencer profile details from the Amazon Influencer store page (e.g. https://www.amazon.com/shop/tastemade).

**端点**: `GET /influencer-profile`


**参数**:

- `influencer_name` (string) *必需*: The Amazon Influencer name for which to get profile details

- `country` (string): Sets the Amazon domain, marketplace country, language and currency. Default: US Allowed values: US, AU, BR, CA, CN, FR, DE, IN, IT, MX, NL, SG, ES, TR, AE, GB, JP, SA, PL, SE, BE, EG, ZA, IE

- `fields` (string): A comma separated list of influencer profile fields to include in the response (field projection). By default all fields are returned. Example: name,profile_link,posts_count,facebook_url

- `language` (string): The language of the results. In case not specified, results will be returned in the default domain language. Supported languages per country: US: en_US, es_US AU: en_AU BR: pt_BR CA: en_CA, fr_CA FR: fr_FR, en_GB DE: de_DE, en_GB, cs_CZ, nl_NL, pl_PL, tr_TR, da_DK IN: en_IN, hi_IN, ta_IN, te_IN, kn_IN, ml_IN, bn_IN, mr_IN IT: it_IT, en_GB MX: es_MX NL: nl_NL, en_GB SG: en_SG ES: es_ES, pt_PT, en_GB TR: tr_TR AE: en_AE, ar_AE GB: en_GB JP: ja_JP, en_US, zh_CN SA: ar_AE, en_AE PL: pl_PL SE: sv_SE,



---


### `products_by_category`

Get products \u0026 offers in a specific Amazon category with pagination support and multiple filters and options such as sort option, price range, product condition filter, and more.

**端点**: `GET /products-by-category`



---


### `seller_profile`

Get Amazon Seller profile details from the Amazon Seller profile page (e.g. https://www.amazon.com/sp?seller=A1D09S7Q0OD6TH).

**端点**: `GET /seller-profile`


**参数**:

- `seller_id` (string) *必需*: The Amazon Seller ID for which to get seller profile details

- `country` (string): Sets the Amazon domain, marketplace country, language and currency. Default: US Allowed values: US, AU, BR, CA, CN, FR, DE, IN, IT, MX, NL, SG, ES, TR, AE, GB, JP, SA, PL, SE, BE, EG, ZA, IE

- `language` (string): The language of the results. In case not specified, results will be returned in the default domain language. Supported languages per country: US: en_US, es_US AU: en_AU BR: pt_BR CA: en_CA, fr_CA FR: fr_FR, en_GB DE: de_DE, en_GB, cs_CZ, nl_NL, pl_PL, tr_TR, da_DK IN: en_IN, hi_IN, ta_IN, te_IN, kn_IN, ml_IN, bn_IN, mr_IN IT: it_IT, en_GB MX: es_MX NL: nl_NL, en_GB SG: en_SG ES: es_ES, pt_PT, en_GB TR: tr_TR AE: en_AE, ar_AE GB: en_GB JP: ja_JP, en_US, zh_CN SA: ar_AE, en_AE PL: pl_PL SE: sv_SE,

- `fields` (string): A comma separated list of seller profile fields to include in the response (field projection). By default all fields are returned. Example: seller_link,phone,business_name,rating



---


### `product_search`

Search for products \u0026 offers on Amazon with pagination support and multiple filters and options such as sort option, price range, product condition filter, and more.

**端点**: `GET /search`


**参数**:

- `query` (string) *必需*: Search query (supports both free-form text queries or a product asin).

- `page` (string): Results page to return. Default: 1

- `country` (string): Sets the Amazon domain, marketplace country, language and currency. Default: US Allowed values: US, AU, BR, CA, CN, FR, DE, IN, IT, MX, NL, SG, ES, TR, AE, GB, JP, SA, PL, SE, BE, EG, ZA, IE

- `sort_by` (string): Return the results in a specific sort order. Default: RELEVANCE Allowed values: RELEVANCE, LOWEST_PRICE, HIGHEST_PRICE, REVIEWS, NEWEST, BEST_SELLERS

- `category_id` (string): Find products in a specific category / department (e.g. computers-intl-ship). Use the Product Category List endpoint to get a list of valid categories and their ids for the country specified in the request. For numeric Amazon category IDs, use the category parameter instead. Default: aps (All Departments)

- `category` (string): Filter by specific numeric Amazon category. The category ID can be obtained from the Amazon category results URL, for example: https://amazon.com/s?node=2858778013 - the Amazon Category ID is 2858778013. Multiple category values can be separated by comma (e.g. categoryId1,categoryId2).

- `min_price` (string): Only return product offers with price greater than a certain value. Specified in the currency of the selected country. For example, in case country=US, a value of 105.34 means $105.34.

- `max_price` (string): Only return product offers with price lower than a certain value. Specified in the currency of the selected country. For example, in case country=US, a value of 105.34 means $105.34.

- `product_condition` (string): Return products in a specific condition. Default: ALL Allowed values: ALL, NEW, USED, RENEWED, COLLECTIBLE

- `brand` (string): Find products with a specific brand. Multiple brands can be specified as a comma (,) separated list. The brand values can be seen from Amazon's search left filters panel, as seen here. Examples: SAMSUNG Google,Apple

- `seller_id` (string): Find products sold by specific seller (merchant). Multiple sellers can be specified as a comma (,) separated list. Examples: A02211013Q5HP3OMSZC7W AM7YCCDZROLB2,A1D09S7Q0OD6TH

- `is_prime` (string): Example value: 

- `deals_and_discounts` (string): Return deals and discounts in a specific condition. Default: NONE Allowed values: NONE, ALL_DISCOUNTS, TODAYS_DEALS

- `four_stars_and_up` (string): Example value: 

- `language` (string): The language of the results. In case not specified, results will be returned in the default domain language. Supported languages per country: US: en_US, es_US AU: en_AU BR: pt_BR CA: en_CA, fr_CA FR: fr_FR, en_GB DE: de_DE, en_GB, cs_CZ, nl_NL, pl_PL, tr_TR, da_DK IN: en_IN, hi_IN, ta_IN, te_IN, kn_IN, ml_IN, bn_IN, mr_IN IT: it_IT, en_GB MX: es_MX NL: nl_NL, en_GB SG: en_SG ES: es_ES, pt_PT, en_GB TR: tr_TR AE: en_AE, ar_AE GB: en_GB JP: ja_JP, en_US, zh_CN SA: ar_AE, en_AE PL: pl_PL SE: sv_SE,

- `additional_filters` (string): Any filters available on the Amazon page but not part of this endpoint's parameters. The filter values can be extracted from the rh parameter in the Amazon search URL after applying the filter of interest on the Amazon search results page. Multiple filters are supported and can be separated by comma (,). For example, when searching for science books with the Paperback book format filter selected, the Amazon URL is: https://www.amazon.com/s?k=science+books&rh=p_n_feature_browse-bin%3A2656022011 a

- `fields` (string): A comma separated list of product fields to include in the response (field projection). By default all fields are returned. Example: product_price,product_url,is_best_seller,sales_volume



---


### `deals`

Get Amazon Deals (Today's Deals / Top Deals, Best Deals, and Lightning Deals) with support for all deal types, filters, and options available on Amazon.

**端点**: `GET /deals-v2`


**参数**:

- `country` (string): Sets the Amazon domain, marketplace country, language and currency. Default: US Allowed values: US, AU, BR, CA, CN, FR, DE, IN, IT, MX, NL, SG, ES, TR, AE, GB, JP, SA, PL, SE, BE, EG, ZA, IE

- `offset` (string): Number of results to skip / index to start from (for pagination).

- `categories` (string): Return deals with products in specific categories / departments. Multiple categories can be specified as a comma (,) separated list. Numeric category id's can be found in the URL after selecting a specific category on https://www.amazon.com/deals. Examples: 502394 2619525011,2617941011

- `min_product_star_rating` (string): Return deals with products star rating greater than a specific value Default: ALL Allowed values: ALL, 1, 2, 3, 4

- `price_range` (string): Return deals with price within a specific price range. 1 is lowest price range shown on Amazon (e.g. Under $25) while 5 is the highest price range (e.g. $200 & Above). Default: ALL Allowed values: ALL, 1, 2, 3, 4, 5

- `discount_range` (string): Return deals with discount within a specific discount range. 1 is lowest discount range shown on Amazon (e.g. 10% off or more) while 5 is the highest discount range (e.g. 70% off or more). Default: ALL Allowed values: ALL, 1, 2, 3, 4, 5

- `brands` (string): Return deals with products by specific brands. Multiple brands can be specified separated by comma (,). In addition, brand names can be found under the Brand filter on the filter/refinements panel on https://www.amazon.com/deals (when applicable). Examples: AQUA CREST Daixers,Antarctic Star

- `prime_early_access` (string): Example value: 

- `prime_exclusive` (string): Example value: 

- `lightning_deals` (string): Example value: 

- `language` (string): The language of the results. In case not specified, results will be returned in the default domain language. Supported languages per country: US: en_US, es_US AU: en_AU BR: pt_BR CA: en_CA, fr_CA FR: fr_FR, en_GB DE: de_DE, en_GB, cs_CZ, nl_NL, pl_PL, tr_TR, da_DK IN: en_IN, hi_IN, ta_IN, te_IN, kn_IN, ml_IN, bn_IN, mr_IN IT: it_IT, en_GB MX: es_MX NL: nl_NL, en_GB SG: en_SG ES: es_ES, pt_PT, en_GB TR: tr_TR AE: en_AE, ar_AE GB: en_GB JP: ja_JP, en_US, zh_CN SA: ar_AE, en_AE PL: pl_PL SE: sv_SE,

- `fields` (string): A comma separated list of deal fields to include in the response (field projection). By default all fields are returned. Example: deal_type,deal_title,deal_ends_at,savings_amount



---



## 技术栈

- **传输协议**: stdio
- **HTTP 客户端**: httpx

## 开发

此服务器由 [API-to-MCP](https://github.com/BACH-AI-Tools/api-to-mcp) 工具自动生成。

版本: 2.0.0

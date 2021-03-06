#!/usr/bin/env python
"""
BuildconfigsetrecordsApi.py
Copyright 2015 Reverb Technologies, Inc.

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.

NOTE: This class is auto generated by the swagger code generator program. Do not edit the class manually.
"""
import sys
import os
import urllib

from models import *


class BuildconfigsetrecordsApi(object):

    def __init__(self, apiClient):
      self.apiClient = apiClient

    
    def getAll(self, **kwargs):
        """Gets all Build Records

        Args:
            
            pageIndex, int: Page index (required)
            
            pageSize, int: Pagination size (required)
            
            sort, str: Sorting RSQL (required)
            
            q, str: RSQL query (required)
            
        Returns: 
        """

        allParams = ['pageIndex', 'pageSize', 'sort', 'q']

        params = locals()
        for (key, val) in params['kwargs'].iteritems():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method getAll" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/build-config-set-records'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'GET'

        queryParams = {}
        headerParams = {}
        formParams = {}
        files = {}
        bodyParam = None

        
        if ('pageIndex' in params):
            queryParams['pageIndex'] = self.apiClient.toPathValue(params['pageIndex'])
        
        if ('pageSize' in params):
            queryParams['pageSize'] = self.apiClient.toPathValue(params['pageSize'])
        
        if ('sort' in params):
            queryParams['sort'] = self.apiClient.toPathValue(params['sort'])
        
        if ('q' in params):
            queryParams['q'] = self.apiClient.toPathValue(params['q'])
        

        

        

        

        

        postData = (formParams if formParams else bodyParam)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams, files=files)
	return response

   
    def getSpecific(self, **kwargs):
        """Gets specific Build Record

        Args:
            
            id, int: BuildConfigSetRecord id (required)
            
        Returns: 
        """

        allParams = ['id']

        params = locals()
        for (key, val) in params['kwargs'].iteritems():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method getSpecific" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/build-config-set-records/{id}'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'GET'

        queryParams = {}
        headerParams = {}
        formParams = {}
        files = {}
        bodyParam = None

        

        

        
        if ('id' in params):
            replacement = str(self.apiClient.toPathValue(params['id']))
            replacement = urllib.quote(replacement)
            resourcePath = resourcePath.replace('{' + 'id' + '}',
                                                replacement)
        

        

        

        postData = (formParams if formParams else bodyParam)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams, files=files)
	return response

   
    def getBuildRecords(self, **kwargs):
        """Gets the build records associated with this set

        Args:
            
            pageIndex, int: Page index (required)
            
            pageSize, int: Pagination size (required)
            
            sort, str: Sorting RSQL (required)
            
            q, str: RSQL query (required)
            
            id, int: Build Config set record id (required)
            
        Returns: 
        """

        allParams = ['pageIndex', 'pageSize', 'sort', 'q', 'id']

        params = locals()
        for (key, val) in params['kwargs'].iteritems():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method getBuildRecords" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/build-config-set-records/{id}/build-records'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'GET'

        queryParams = {}
        headerParams = {}
        formParams = {}
        files = {}
        bodyParam = None

        
        if ('pageIndex' in params):
            queryParams['pageIndex'] = self.apiClient.toPathValue(params['pageIndex'])
        
        if ('pageSize' in params):
            queryParams['pageSize'] = self.apiClient.toPathValue(params['pageSize'])
        
        if ('sort' in params):
            queryParams['sort'] = self.apiClient.toPathValue(params['sort'])
        
        if ('q' in params):
            queryParams['q'] = self.apiClient.toPathValue(params['q'])
        

        

        
        if ('id' in params):
            replacement = str(self.apiClient.toPathValue(params['id']))
            replacement = urllib.quote(replacement)
            resourcePath = resourcePath.replace('{' + 'id' + '}',
                                                replacement)
        

        

        

        postData = (formParams if formParams else bodyParam)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams, files=files)
	return response

   

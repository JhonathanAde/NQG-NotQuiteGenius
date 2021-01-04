import React, { useState } from 'react';
import { NavLink } from 'react-router-dom';
import './Search.css'

const Search = ({clearSearch, lastSearch, setLastSearch}) => {
  const [results, setResults] = useState([]);
  const [doingSearch, setDoingSearch] = useState(false);
  const [inputValue, setInputValue] = useState(lastSearch);
  const [noResultsMsg, setNoResultsMessage] = useState(false)

  const doSearch = (e) => {
    e.stopPropagation();
    const value = document.getElementById('search').value;
    if (value) {
      setLastSearch(value);
      setResults([]);
      setNoResultsMessage(false);
      setDoingSearch(true);
      sizeResults('min');
      (async () => {
        const response = await fetch(`/api/search?search_string=${value}`,
        {
          method: 'GET',
          headers: {
            'Content-Security-Policy': 'upgrade-insecure-requests'
          },
        });
        const res = await response.json();
        setDoingSearch(false);
        // console.log(res)
        if (res.results.length) {
          setResults(res.results);
        } else {
          setNoResultsMessage(true)
        }
        sizeResults('full');
      })();
    }
  }

  const displaySearchInfo = (e) => {
    document.getElementById('search-results').style.display = 'block';
    document.getElementById('search').value = inputValue
    sizeResults(results.length ? 'full' : 'min');

  }

  const hideSearchInfo = (e) => {
    e.stopPropagation()
    document.getElementById('search').value = lastSearch
    clearSearch(e);
  }

  const sizeResults = (size) => {
    if (size === 'min') {
      document.getElementById('search-results').style.bottom = 'auto';
    } else {
      document.getElementById('search-results').style.bottom = null;
    }
  }

  const updateInput = (e) => {
    setInputValue(e.target.value)
  }


  return (
    <div className="search-container" onClick={displaySearchInfo} >
      <input id="search" type="search" className="search-bar" placeholder="search" autoComplete="off" onChange={updateInput} value={inputValue}/>
      <button className="search-button" onClick={doSearch}><i className="fas fa-search"></i></button>
      <div id="search-results">
        <p className="search-help">For searching, use double quotes if you desire exact phrases or words (including capitalization and punctuation). (Note: usernames are currently not searchable.)<span className="search-close" onClick={hideSearchInfo}><i className="fas fa-times-circle"></i></span></p>
        { (results.length &&
          <>
            <h2>Last search was: <span className="search-msg">{lastSearch}</span></h2>

            <ul className="search-results-list">
                {results.map((link) => (
                  <li className="search-results-item">
                    <NavLink className="search-link" to={`${link.url}`} key={`${link.key}`} onClick={hideSearchInfo}>
                      {link.display}
                    <span className="search-info"> (Hits in: {link.hitLocations})</span>
                    </NavLink>
                  </li>
                ))}
            </ul>
          </>
          )
          ||
          (doingSearch &&
          <h2>Searching ...</h2>
          )
          ||
          (noResultsMsg &&
          <>
            <h2>No results searching for: <span className="search-msg">{lastSearch}</span></h2>
          </>
          )
        }
      </div>
    </div>
  )
}

export default Search

import React, { useState, useEffect } from 'react';
import { NavLink } from 'react-router-dom';
import './Search.css'

const Search = ({clearSearch, lastSearch, setLastSearch}) => {
  const [results, setResults] = useState([]);
  const [doingSearch, setDoingSearch] = useState(false);
  const [inputValue, setInputValue] = useState(lastSearch);
  const [noResultsMsg, setNoResultsMessage] = useState([])

  // useEffect(() => {

  // }, [results])

  const doSearch = (e) => {
    e.stopPropagation();
    const value = document.getElementById('search').value;
    if (value) {
      setLastSearch(value);
      setResults([]);
      setNoResultsMessage([]);
      setDoingSearch(true);
      sizeResults();
      (async () => {
        const response = await fetch(`/api/search?search_string=${value}`);
        const res = await response.json();
        setDoingSearch(false);
        console.log(res)
        if (res.results.length) {
          await setResults(res.results);
        } else {
          await setNoResultsMessage([`No results for searching for:`, `${value}`])
        }
        sizeResults();
      })();
    }
  }

  const displaySearchInfo = (e) => {
    document.getElementById('search-results').style.display = 'block';
    document.getElementById('search').value = inputValue
    sizeResults();
  }

  const hideSearchInfo = (e) => {
    document.getElementById('search').value = lastSearch
    clearSearch();
  }

  const sizeResults = () => {
    if (!results.length) {
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
        <p className="search-help">For searching, use double quotes around exact phrases or words.</p>
        { (results.length &&
          <>
            <h2>Search for: {lastSearch}</h2>
            <ul className="search-results-list">
                {results.map((link) => (
                  <li className="search-results-item">
                    <NavLink className="search-link" to={`${link.url}`} key={`${link.key}`} onClick={clearSearch}>
                      {link.display}
                    </NavLink>
                    <span className="search-info">(Hits in: {link.locations.toString()})</span>
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
            <h2>{noResultsMsg[0]}</h2>
            <div className="search-no-result">{noResultsMsg[1]}</div>
          </>
          )
        }
      </div>
    </div>
  )
}

export default Search

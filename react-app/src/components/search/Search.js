import React, { useState, useEffect } from 'react';
import { NavLink } from 'react-router-dom';
import './Search.css'

const Search = () => {
  const [results, setResults] = useState([]);

  // useEffect(() => {

  // }, [results])

  const doSearch = (e) => {
    e.stopPropagation();
    const value = document.getElementById('search').value;
    if (value) {
      (async () => {
        const response = await fetch(`/api/search?search_string=${value}`);
        const res = await response.json();
        console.log(res)
        setResults(res.results)
      })();
    }
  }

  const displaySearchInfo = (e) => {
    document.getElementById('search-results').style.display = 'block';
  }

  return (
    <div className="search-container" onClick={displaySearchInfo} >
      <input id="search" type="search" className="search-bar" placeholder="search" />
      <button className="search-button" onClick={doSearch}><i className="fas fa-search"></i></button>
      <div id="search-results">
        { results &&
        <ul className="search-results-list">
            {results.map((link) => (
              <li className="search-results-item">
                <NavLink className="search-link" to={`${link.url}`} key={`${link.key}`}>
                  {link.display}
                </NavLink>
                <div className="search-info">Hits in: </div>
              </li>
            ))}
        </ul>
        }
      </div>
    </div>
  )
}

export default Search

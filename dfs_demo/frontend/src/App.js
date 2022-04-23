import React from 'react';
import axios from 'axios';
import './App.css';
import ReactDOM from 'react-dom/client';

export default class App extends React.Component {
  state = {
    details: []
  }

  componentDidMount() {
    axios.get(`http://127.0.0.1:8000/dfs_app_dfs_model_covid`)
      .then(res => {
        const details = res.data;
        this.setState({ details });
      })
  }

  render() {
    return (
      // <div>Hello</div>
      <table className='dfs_table'>
        <tr>
            <th> ID </th>
            <th>Patient_id</th>
            <th>Sample_id</th>
            <th>Country</th>
            <th>Site_id</th>
            <th>Timestamp</th>
        </tr>
        {
          // console.log(this.state.details)
          this.state.details
            .map(detail =>
              <tr>
                <td key={detail.id}>{detail.id}</td>
                <td key={detail.id}>{detail.timestamp}</td>
                <td key={detail.id}>{detail.patient_id}</td>
                <td key={detail.id}>{detail.sample_id}</td>
                <td key={detail.id}>{detail.country}</td>
                <td key={detail.id}>{detail.site_id}</td>
              </tr>
              
            )
        }
      </table>
      

      // <tbody>
      //   <tr>
      //       <th> ID </th>
      //       <th>Patient_id</th>
      //       <th>Sample_id</th>
      //       <th>Country</th>
      //       <th>Site_id</th>
      //       <th>Timestamp</th>
      //   </tr>
        
      //   <tr>
      //   {
      //     this.state.details
      //       .map(detail =>
      //         { console.log(detail);
      //           return (
      //             <td key={detail.id}>{detail.name}</td> )}
      //       )
      //   }
      //   </tr>
      //   </tbody>
    )
  }
}